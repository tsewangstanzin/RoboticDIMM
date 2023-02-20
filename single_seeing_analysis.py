import sys
import os
import numpy as np
import scipy.ndimage as nd
from astropy.io import fits as pyfits
from datetime import datetime, timedelta
from photutils.aperture import aperture_photometry
from astropy.stats import sigma_clipped_stats
from photutils.detection import find_peaks
from photutils.detection import DAOStarFinder,IRAFStarFinder
from astropy.table.pprint import conf
from photutils.aperture import CircularAperture
from photutils.centroids import centroid_sources, centroid_com, centroid_2dg, centroid_1dg, centroid_quadratic
conf.max_lines = -1
conf.max_width = -1
np.set_printoptions(threshold=sys.maxsize)
import warnings
warnings.filterwarnings("ignore")

class Seeing:
    def __init__(self,cube_3d_array,fits_file_name):
        self.cube_3d_array = cube_3d_array
        self.fits_file_name=fits_file_name
        '''DIMM computation constants'''
        #self.pixel_scale = 0.50077  #Basler
        #self.pixel_scale = 0.699  #Old CMOS 3by3 binning, pixel scale in arcsec.
        self.pixel_scale = 0.233*3  # New CMOS 2by2 binning, pixel scale in arcsec.   3 is the binning
        self.rd = 0.242665  # hole separation in meter
        self.d = 0.05494  # hole dia
        self.lamb = 0.5 / 1000000  # 0.65e-6   #wavelength
        self.b = self.rd / self.d
        self.x1 = []
        self.y1 = []
        self.c1 = []
        self.c2 = []
        self.d1 = []
        self.d2 = []
        self.x2 = []
        self.y2 = []
        self.fwhm1=[]
        self.sharpness1=[]
        self.roundness1=[]
        self.peak_count1=[]
        self.fwhm2=[]
        self.sharpness2=[]
        self.roundness2=[]
        self.peak_count2=[]

        self.last_c1=0
        self.last_c2=0
        self.starnotfound=0
        return None
    def working_directory(self):
        now = datetime.now()
        date_today = now.strftime("%Y%m%d")
        date_today = datetime.strptime(date_today, "%Y%m%d")
        start_time = date_today + timedelta(hours=10)
        datetime_now = datetime.now()
        if start_time > datetime_now:
            createfolder_flag = 0
        else:
            createfolder_flag = 1
        if createfolder_flag == 1:
            self.WorkingDir = now.strftime("%Y%m%d")
        else:
            yesterday_date = date_today - timedelta(hours=24)
            yesterday_date = yesterday_date.strftime("%Y%m%d")
            self.WorkingDir = yesterday_date
        return self.WorkingDir
    def compute(self,wd):
        current_time = datetime.now()
        #file_n=str(current_time.year)+str("_")+str(current_time.month)+str("_")+str(current_time.day)+str("_")+str(current_time.hour)+str("_")+str(current_time.minute)+str("_")+str(current_time.second)+str("_")+str(current_time.microsecond)+"_Centeroids.dat"
   
        cube_name = os.path.basename(self.fits_file_name)
        file = os.path.splitext(cube_name)
        file_n=file[0]+".dat"
        
        centroid_filename= str(wd)+str("/")+file_n
        f = open(centroid_filename, 'w')
        f.write("#FITSName Image_No X1 Y1 X2 Y2 CenterX CenterY FWHM_S1 FWHM_S2 SHARPNESS_S1 SHARPNESS_S2 ROUNDNESS_S1 ROUNDNESS_S2 PEAK_S1 PEAK_S2 INTENSITY_S1 INTENSITY_S2\n" )
        for i in range( self.cube_3d_array.shape[0]):
            #n, centroids = self.starfind_method1( self.cube_3d_array[i])
            #hdul = pyfits.open('testimage.fits')  # Open image
            #dat = hdul[0].data  # data = pixel brightness
            #n, centroids, fwhm, sharpness, roundness, peak_count=self.starfind_method2(self.cube_3d_array[i])
            n, centroids, fwhm, sharpness, roundness, peak_count=self.starfind_method2((self.cube_3d_array[i]))
            #print("Number of star found in this :",n)
            #n,centroids = self.starfind_method1(self.cube_3d_array[i])
            #centroids=[[centroids[0][1],centroids[0][0]],[centroids[1][0],centroids[1][1]]]
            img22 =  self.cube_3d_array[i]
            #img22 = dat
            if n == 2:
                #print("DIMM Star found")
                #print(str("DIMM Star found at image number:")+str(i+1)+"  "+centroids , end = "\r")
                #print(i+1, centroids)
                self.x_1 = float(centroids[0][0])
                self.y_1 = float(centroids[0][1])
                self.x_2 = float(centroids[1][0])
                self.y_2 = float(centroids[1][1])
                #aperture = CircularAperture(centroids, r=10.)
                #phot_table = aperture_photometry(img22, aperture)
                #star1_intensity = float(phot_table[0]['aperture_sum'])
                #star2_intensity=float(phot_table[1]['aperture_sum'])
                #Method2 without package
                star1_intensity = np.sum(img22[int(self.y_1):int(self.y_1) + 10, int(self.x_1):int(self.x_1) + 10])    #total intensity around 10 pixel of centroid 1
                star2_intensity = np.sum(img22[int(self.y_2):int(self.y_2) + 10, int(self.x_2):int(self.x_2) + 10]) #Center distance of two star stars
                xsum = 0.0
                ysum = 0.0
                for star in centroids:
                    (x, y) = star
                    #(y, x) = star
                    xsum += x
                    ysum += y
                center_x = xsum / 2
                center_y = ysum / 2
                f.write("%s %d %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f \n" % (self.fits_file_name,i+1,
                                                          float(centroids[0][0]), float(centroids[0][1]), float(centroids[1][0]), float(centroids[1][1]),
                                                          center_x,center_y,
                                                          fwhm[0],fwhm[1],
                                                          sharpness[0],sharpness[1],
                                                          roundness[0],roundness[1],
                                                          peak_count[0], peak_count[1],
                                                          star1_intensity,star2_intensity))
                #Append to vector list. Need after the loop
                self.last_c1=center_x
                self.last_c2=center_y
                self.y1.append(centroids[0][1])
                self.x1.append(centroids[0][0])
                self.y2.append(centroids[1][1])
                self.x2.append(centroids[1][0])
                self.d1.append(star1_intensity)
                self.d2.append(star2_intensity)
                self.c1.append(center_x)
                self.c2.append(center_y)
                self.fwhm1.append(fwhm[0])
                self.fwhm2.append(fwhm[1])
                self.sharpness1.append(sharpness[0])
                self.sharpness2.append(sharpness[1])
                self.roundness1.append(roundness[0])
                self.roundness2.append(roundness[1])
                self.peak_count1.append(peak_count[0])
                self.peak_count2.append(peak_count[1])
                print(str("DIMM star found at image number:") + str(i + 1))

            else:
                 self.starnotfound=self.starnotfound+1
                 print(str("No DIMM star found at image number:") + str(i + 1),n)
                 #print(str("No DIMM star found at image number:")+str(i+1), end = "\r")
        f.close()
        print("\nCube Size: ",self.cube_3d_array.shape[0])
        print("\nNo. of Usable data points: ", self.cube_3d_array.shape[0]-self.starnotfound)
        #if(self.starnotfound>70):
        #    os.remove(filename)
        #Arrays
        self.y1 = np.array(self.y1)
        self.y2 = np.array(self.y2)
        self.x1 = np.array(self.x1)
        self.x2 = np.array(self.x2)
        # Array of center distance between two stars
        self.c1=np.array(self.c1)
        self.c2=np.array(self.c2)
        # Array of star intensity
        self.d1=np.array(self.d1)
        self.d2=np.array(self.d2)
        self.fwhm1 = np.array(self.fwhm1)
        self.sharpness1 = np.array(self.sharpness1)
        self.roundness1 = np.array(self.roundness1)
        self.peak_count1 = np.array(self.peak_count1)
        self.fwhm2 = np.array(self.fwhm2)
        self.sharpness2 = np.array(self.sharpness2)
        self.roundness2 = np.array(self.roundness2)
        self.peak_count2 = np.array(self.peak_count2)
        return  self.x2 ,self.y2 ,self.x1 ,self.y1,self.c1,self.c2,self.d1,self.d2,self.starnotfound,self.last_c1,self.last_c2, \
                self.fwhm1 ,\
                self.sharpness1,\
                self.roundness1,\
                self.peak_count1, \
                self.fwhm2, \
                self.sharpness2, \
                self.roundness2, \
                self.peak_count2, \
                file_n

    def starfind_method1(self,im):
        mean = np.mean(im)
        sig = np.std(im)
        smooth = nd.gaussian_filter(im, 3.0)
        print(mean,sig, np.max(im))
        clip_data=smooth >= (mean + 50.0)
        clip = clip_data
        labels, num = nd.label(clip)
        print(np.max(labels))
        pos = nd.center_of_mass(im, labels, range(num + 1))
        centroids=pos[1:]
        if(num==2):
            x1=centroids[0][1]
            y1 = centroids[0][0]
            x2 = centroids[1][1]
            y2 = centroids[1][0]
            print("x1,y1,x2,y2",x1,y1,x2,y2)
            centroids = [[x1, y1], [x2, y2]]
            if (float(x1) > float(x2)):
                print("\n \n \n Star 2 found before Star1, rearranging")
                centroids = [[x2, y2], [x1, y1]]
                print("\n \n \n Rearranged",centroids)
            fwhm = []
            sharpness = []
            roundness = []
            peak_count = []
            fwhm = [0, 0]
            sharpness = [0, 0]
            roundness = [0, 0]
            peak_count = [0, 0]
        else:
            centroids = [[0, 0], [0, 0]]
            num=1
            fwhm = [0, 0]
            sharpness = [0, 0]
            roundness = [0, 0]
            peak_count = [0, 0]
        return num, centroids ,fwhm,sharpness,roundness,peak_count
    def starfind_method2(self,im):
        data = im
        mean, median, std = sigma_clipped_stats(data, sigma=3.0)
        #print((mean, median, std))
        starfind = IRAFStarFinder(fwhm=6.0, threshold=100.0,  sharplo=-10.0, sharphi=10.0, roundlo=-10.0, roundhi=10.0)
        sources = starfind(data-median)
        centroids=[]
        fwhm=[]
        sharpness=[]
        roundness=[]
        peak_count = []
        if(str(type(sources))!="<class 'NoneType'>"):
            n=len(sources)
            if(n==2):
                for i in range (n):
                    centroids.append([float(sources[i]['xcentroid']),float(sources[i]['ycentroid'])])
                    fwhm.append(float(sources[i]['fwhm']))
                    sharpness.append(float(sources[i]['sharpness']))
                    roundness.append(float(sources[i]['roundness']))
                    peak_count.append(float(sources[i]['sky'])+float(sources[i]['peak']))
                #threshold = median + (5. * std)
                #tbl = find_peaks(data, threshold, box_size=11)
                #for i in range (len(tbl)):
                #    peak_count.append(float(tbl[i]['peak_value']))
                # This condition below is important as sometimes the algorithm find STAR2 earlier than STAR1
                # messing the x1,y1 and x2,y2 array
                if(centroids[0][0]>centroids[1][0]):
                    centroids=[[centroids[1][0],centroids[1][1]],[centroids[0][0],centroids[0][1]]]
                    fwhm=[fwhm[1],fwhm[0]]
                    sharpness=[sharpness[1],sharpness[0]]
                    roundness=[roundness[1],roundness[0]]
                    peak_count=[peak_count[1],peak_count[0]]
                #positions = np.transpose((sources['xcentroid'], sources['ycentroid']))
                #apertures = CircularAperture(positions, r=4.)
                #norm = ImageNormalize(stretch=SqrtStretch())
                # plt.imshow(data, cmap='Greys', origin='lower', norm=norm,
                #           interpolation='nearest')
                # plt.show()
                #print("Centroiding layer 1:")
                #print(centroids)
                # data = make_4gaussians_image()
                x_init = (int(centroids[0][0]), int(centroids[1][0]))
                y_init = (int(centroids[0][1]), int(centroids[1][1]))
                # Functions avaialable: centroid_2dg() centroid_1dg() centroid_quadratic() centroid_com()
                x, y = centroid_sources(data, x_init, y_init, box_size=21,
                                        centroid_func=centroid_com)
                #print("Centroiding layer 2:")
                centroids = [[x[0], y[0]], [x[1], y[1]]]
                #print(centroids)
                #print(fwhm)
                #print(centroids)
                #print(sharpness)
                #print(roundness)
                #print(peak_count)
                #print("Method 2:   IRAFStarFind algorithm")
                #print(n)
                #print((centroids[0][1]), (centroids[0][0]), (centroids[1][1]), (centroids[1][0]))
            else:
                n=1
                centroids = [[0,0],[0,0]]
                fwhm = [0, 0]
                sharpness = [0, 0]
                roundness = [0, 0]
                peak_count = [0, 0]
        else:
            n=0
            centroids = [[0,0],[0,0]]
            fwhm = [0,0]
            sharpness = [0,0]
            roundness = [0,0]
            peak_count = [0,0]
        return n,centroids,fwhm,sharpness,roundness,peak_count
    def starfind_method3(self,im):
        data = im
        mean, median, std = sigma_clipped_stats(data, sigma=3.0)
        #print((mean, median, std))
        starfind=DAOStarFinder(fwhm=3.0, threshold=10. * std)
        sources = starfind(data-median)
        #print(sources)
        n=len(sources)
        centroids=[]
        roundness=[]
        for i in range (len(sources)):
            centroids.append([float(sources[i]['ycentroid']),float(sources[i]['xcentroid'])])
            roundness.append(float(sources[i]['roundness1']))
        #print(fwhm)
        #print(centroids)
        #print(sharpness)
        #print(roundness)
        #print(roundness)
        threshold = median + (5. * std)
        tbl = find_peaks(data, threshold, box_size=11)
        peak_count=[]
        for i in range (len(tbl)):
            peak_count.append(float(tbl[i]['peak_value']))
        #print(peak_star)
        #print("Method 3:   DAOStarFind algorithm")
        #print(n)
        #print((centroids[0][1]), (centroids[0][0]), (centroids[1][1]), (centroids[1][0]))
        return n,centroids,roundness,peak_count

    def seeing_saravin_x(self,v):
        #1 pixel is pixel_scal.206262 radian   radian square
        v = v * (self.pixel_scale / 206265.0) ** 2.0       #variance in radian square
        k = 0.364 * (1.0 - 0.532 * self.b ** (-1.0 / 3.0) - 0.024 * self.b ** (-7.0 / 3.0))       #Horizontal /Longitudenal
        seeing = 206265.0 * 0.98 * ((self.d / self.lamb) ** 0.2) * ((v / k) ** 0.6)
        #seeing = 206265.0 * 0.98 * (np.cos(z)**-0.6) * ((d / lamb) ** 0.2) * ((v / k) ** 0.6)   #Zenith Distance correction (not included for now)
        return seeing
    def seeing_saravin_y(self,v):
        v = v * (self.pixel_scale / 206265.0) ** 2.0
        k = 0.364 * (1 - 0.798 * self.b ** (-1.0 / 3.0) + 0.018 * self.b ** (-7.0 / 3.0))    #Vertical   /Traversal
        seeing = 206265.0 * 0.98 * ((self.d / self.lamb) ** 0.2) * ((v / k) ** 0.6)
        #206265 is for radian to arcsecond
        #seeing = 206265.0 * 0.98 * (np.cos(z) ** -0.6) * ((d / lamb) ** 0.2) * ((v / k) ** 0.6)  # Zenith Distance correction (not included for now)
        return seeing
    def seeing_fried_x(self,v):
        v = v * (self.pixel_scale / 206265.0) ** 2.0
        r0 = (2.0 * self.lamb * self.lamb * (0.1790 * (self.d ** (-1.0 / 3.0)) -0.0968 * (self.rd ** (-1.0 / 3.0))) / v) ** 0.6
        seeing = 206265.0 * 0.98 * self.lamb / r0
        #seeing = 206265.0 * 0.98 *(np.cos(z) ** -0.6)* lamb / r0
        return seeing
    def seeing_fried_y(self,v):
        v = v * (self.pixel_scale / 206265.0) ** 2.0
        r0 = (2.0 * self.lamb * self.lamb * (0.1790 * (self.d ** (-1.0 / 3.0)) -0.145 * (self.rd ** (-1.0 / 3.0))) / v) ** 0.6
        seeing = 206265.0 * 0.98 * self.lamb / r0
        #seeing = 206265.0 * 0.98 * (np.cos(z) ** -0.6)* lamb / r0
        return seeing
def main():
    #pass
    #For StandAlone Analysis operation, Uncomment the below and comment the pass
    print("-----------Image Analyser----------")
    filename = input("Drag and drop a cube file for computing seeing: \n")
    filename = filename.replace("'", "")
    filename = filename.replace(" ", "")

    hdul = pyfits.open(filename)  # Open image
    dat = hdul[0].data  # data = pixel brightness
    #print(dat)
    analysis=Seeing(dat,filename)
    
    #For test Keep 
    #wd=analysis.working_directory()
    wd='DIMManalysis'
    if not os.path.exists(wd):
            os.mkdir(wd)
    
  
    x2, y2, x1, y1, c1, c2, d1, d2, starnotfound, last_c1, last_c2, fwhm1, sharpness1, roundness1, peak_count1, fwhm2, sharpness2, roundness2, peak_count2, cent_filename = analysis.compute(wd)
    now = datetime.now()
    f2 = open(str(wd) + '/Seeing_Tokovin.dat', 'a')
    f3 = open(str(wd) + '/Seeing_Fried.dat', 'a')
    if (os.stat(str(wd) + '/Seeing_Tokovin.dat').st_size == 0):
        f2.write(
            "#CENTFILE DATE TIME VAR_X VAR_Y MEAN_CENTER_X MEAN_CENTER_Y MEAN_INTENSITY_1 MEAN_INTENSITY_1 REJECTED_STARS MEAN_FWHM_1 MEAN_FWHM_2 MEAN_SHARPNESS_1 MEAN_SHARPNESS_2 MEAN_ROUNDNESS_1 MEAN_ROUNDNESS_2 MEAN_PEAK_1 MEAN_PEAK_2 SEEING_X SEEING_Y\n")
    if (os.stat(str(wd) + '/Seeing_Fried.dat').st_size == 0):
        f3.write(
            "#CENTFILE DATE TIME VAR_X VAR_Y MEAN_CENTER_X MEAN_CENTER_Y MEAN_INTENSITY_1 MEAN_INTENSITY_1 REJECTED_STARS MEAN_FWHM_1 MEAN_FWHM_2 MEAN_SHARPNESS_1 MEAN_SHARPNESS_2 MEAN_ROUNDNESS_1 MEAN_ROUNDNESS_2 MEAN_PEAK_1 MEAN_PEAK_2 SEEING_X SEEING_Y\n")
    if (starnotfound < 50):
        # Variance over x and y axis
        varx = np.var(np.sqrt(abs(x2 - x1) ** 2))
        vary = np.var(np.sqrt(abs(y2 - y1) ** 2))
        # Combined variance
        r = np.sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
        var = np.var(r)
        print("\n\n\nVarX = %f, VarY = %f, Combined vAr= %f" % (varx, vary, var))
        # Seeing Method 1 tokovin
        seeing_x_saravin = float(analysis.seeing_saravin_x(varx))
        seeing_y_saravin = float(analysis.seeing_saravin_y(vary))
        print("Saravin:  Seeing X = %f, Seeing Y = %f" % (seeing_x_saravin, seeing_y_saravin))
        f2.write("%s %s %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f\n" % (
            cent_filename, now, varx, vary, np.mean(c1), np.mean(c2), np.mean(d1), np.mean(d2), starnotfound,
            np.mean(fwhm1), np.mean(fwhm2),
            np.mean(sharpness1), np.mean(sharpness2), np.mean(roundness1), np.mean(roundness2), np.mean(peak_count1),
            np.mean(peak_count2), seeing_x_saravin, seeing_y_saravin))
        # Star Related self.ra, self.dec, self.airmass,seeing_x_saravn with Airmass correction  tel_alt
        # Seeing Method 1 Saravin
        seeing_x_fried = float(analysis.seeing_fried_x(varx))
        seeing_y_fried = float(analysis.seeing_fried_y(vary))
        print("Fried:  Seeing X = %f, Seeing Y = %f" % (seeing_x_fried, seeing_y_fried))
        f3.write("%s %s %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f\n" % (
            cent_filename, now, varx, vary, np.mean(c1), np.mean(c2), np.mean(d1), np.mean(d2), starnotfound,
            np.mean(fwhm1), np.mean(fwhm2),
            np.mean(sharpness1), np.mean(sharpness2), np.mean(roundness1), np.mean(roundness2), np.mean(peak_count1),
            np.mean(peak_count2), seeing_x_fried,
            seeing_y_fried))
    else:
        print("\n")
        print("Data not usable (Its either wind/cloud).... DIMM star not found in: %d images" %(starnotfound))

    print("Centroid Log:\n", str(wd)+'/'+cent_filename)
    print("Seeing Log:\n", str(wd) + '/Seeing_Tokovin.dat', str(wd) + '/Seeing_Fried.dat')
    f2.close()
    f3.close()

if __name__ == "__main__":
    main()









