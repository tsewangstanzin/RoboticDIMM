import sys
import os
import numpy as np
import scipy.ndimage as nd
from astropy.io import fits as pyfits
import glob
from datetime import datetime, timedelta
import time
from photutils.aperture import CircularAperture
from photutils.aperture import aperture_photometry
import photutils
import pandas as pd
from astropy.stats import sigma_clipped_stats
from photutils.datasets import load_star_image
from astropy.stats import sigma_clipped_stats
from photutils.datasets import make_100gaussians_image
from photutils.detection import find_peaks
from photutils.detection import DAOStarFinder,IRAFStarFinder
from astropy.table.pprint import conf
import matplotlib.pyplot as plt
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from photutils.aperture import CircularAperture
import matplotlib.pyplot as plt
from photutils.centroids import centroid_sources, centroid_com, centroid_2dg, centroid_1dg, centroid_quadratic
from photutils.datasets import make_4gaussians_image
conf.max_lines = -1
conf.max_width = -1

np.set_printoptions(threshold=sys.maxsize)

class Seeing:
    def __init__(self,cube_3d_array,fits_file_name):
        self.cube_3d_array = cube_3d_array
        self.fits_file_name=fits_file_name
        #print(self.cube_3d_array)

        '''DIMM computation constants'''
        #self.pixel_scale = 0.50077  #Basler
        #self.pixel_scale = 0.699  #Old CMOS 3by3 binning, pixel scale in arcsec.
        self.pixel_scale = 0.46692  # New CMOS 2by2 binning, pixel scale in arcsec.
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
        #For zenith distance correction
        #star_alt=90
        #zdeg = 90-star_alt # angle between star to zenith (deg)
        #z = (zdeg*np.pi)/180 # angle in rad
        #print((np.cos(z)**0.6))   #Multiply this to seeing!! Its acting opposite!
        return None
    def compute(self,wd):
        current_time = datetime.now()
        file_n=str(current_time.year)+str("_")+str(current_time.month)+str("_")+str(current_time.day)+str("_")+str(current_time.hour)+str("_")+str(current_time.minute)+str("_")+str(current_time.second)+str("_")+str(current_time.microsecond)+"_Centeroids.dat"
        filename= str(wd)+str("/")+file_n
        f = open(filename, 'w')
        f.write("#FITSName Image_No X1 Y1 X2 Y2 CenterX CenterY FWHM_S1 FWHM_S2 SHARPNESS_S1 SHARPNESS_S2 ROUNDNESS_S1 ROUNDNESS_S2 PEAK_S1 PEAK_S2 INTENSITY_S1 INTENSITY_S2\n" )
        print("\n")
        for i in range( self.cube_3d_array.shape[0]):
            #n, centroids = self.starfind_method1( self.cube_3d_array[i])
            #hdul = pyfits.open('testimage.fits')  # Open image
            #dat = hdul[0].data  # data = pixel brightness

            n, centroids, fwhm, sharpness, roundness, peak_count=self.starfind_method2(self.cube_3d_array[i])
            #n,centroids = self.starfind_method1(self.cube_3d_array[i])
            #centroids=[[centroids[0][1],centroids[0][0]],[centroids[1][0],centroids[1][1]]]
            img22 =  self.cube_3d_array[i]
            #img22 = dat
            if n == 2:
                #print("DIMM Star found")
                #print(str("DIMM Star found at image number:")+str(i+1)+"  "+centroids , end = "\r")
                print(i+1, centroids)
                self.x_1 = float(centroids[0][0])
                self.y_1 = float(centroids[0][1])
                self.x_2 = float(centroids[1][0])
                self.y_2 = float(centroids[1][1])
                aperture = CircularAperture(centroids, r=10.)
                phot_table = aperture_photometry(img22, aperture)
                star1_intensity = float(phot_table[0]['aperture_sum'])
                star2_intensity=float(phot_table[1]['aperture_sum'])
                #Method2 without package
                #star1_intensity = np.sum(img22[self.y_1:self.y_1 + 10, self.x_1:self.x_1 + 10])    #total intensity around 10 pixel of centroid 1
                #star2_intensity = np.sum(img22[self.y_2:self.y_2 + 10, self.x_2:self.x_2 + 10])    #total np.max() if max intensity around 10 pixel of centroid 2
                #Center distance of two star stars
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

            else:
                 self.starnotfound=self.starnotfound+1
                 print(str("No DIMM star/more than 2 stars found at image number:")+str(i+1), end = "\r")
        f.close()
        if(self.starnotfound>150):
            os.remove(filename)

        # LOOP over 300 cube ends
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
        #print(sig)
        clip_data=smooth >= (mean + 5.0)
        clip = clip_data
        labels, num = nd.label(clip)
        pos = nd.center_of_mass(im, labels, range(num + 1))
        centroids=pos[1:]
        #print("Method 1: Weighted average algorithm")
        #print (num)
        #print((centroids[0][1]),(centroids[0][0]),(centroids[1][1]),(centroids[1][0]))
        return num, pos[1:]

    def starfind_method2(self,im):
        data = im
        mean, median, std = sigma_clipped_stats(data, sigma=3.0)
        #print((mean, median, std))

        starfind = IRAFStarFinder(fwhm=3.0, threshold=10. * std, sigma_radius=1.5, minsep_fwhm=2.0, sharplo=-10.0, sharphi=10.0, roundlo=-10.0, roundhi=10.0, sky=None, exclude_border=False, brightest=None, peakmax=None)
        sources = starfind(data-median)
        #print(type(sources))
        centroids=[]
        fwhm=[]
        sharpness=[]
        roundness=[]
        peak_count = []
        if(str(type(sources))!="<class 'NoneType'>"):
            n=len(sources)
            #print(sources)

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
    #For StandAlone Grabber operation, Uncomment the below and comment the pass
    print("-----------Image Analyser----------")
    '''
    hdul = pyfits.open('testimage.fits')  # Open image
    dat = hdul[0].data  # data = pixel brightness
    grabber=Seeing(100)
    grabber.starfind_method1(dat)
    grabber.starfind_method2(dat)
    grabber.starfind_method3(dat)
    '''
if __name__ == "__main__":
    main()









