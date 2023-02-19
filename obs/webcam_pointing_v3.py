from __future__ import print_function
import cv2
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta
import ephem
import numpy as np
import time
import pysftp
import pytz
from imutils import contours
from skimage import measure
import imutils

import numpy
import sys
import os
import numpy as np
import scipy.ndimage as nd
from astropy.io import fits as pyfits
import glob
import cv2
import datetime
import time
from photutils.aperture import CircularAperture
from photutils.aperture import aperture_photometry
from photutils.datasets import make_100gaussians_image
from photutils.detection import find_peaks
from photutils.detection import DAOStarFinder, IRAFStarFinder
from astropy.stats import sigma_clipped_stats
from photutils.datasets import load_star_image
from astropy.stats import sigma_clipped_stats
import matplotlib.pyplot as plt
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from photutils.aperture import CircularAperture
import ephem
import re
import sys, select, os
import subprocess
import socket
from astropy.stats import sigma_clipped_stats
from photutils.detection import DAOStarFinder,IRAFStarFinder
from astropy.table.pprint import conf
import matplotlib.pyplot as plt
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from photutils.aperture import CircularAperture
import matplotlib.pyplot as plt
from photutils.centroids import centroid_sources, centroid_com, centroid_2dg, centroid_1dg, centroid_quadratic
from photutils.datasets import make_4gaussians_image
import sys
import os
import numpy as np
import scipy.ndimage as nd
from astropy.io import fits as pyfits
import glob
from datetime import datetime, timedelta
import time
from meade_tel_control import Telescope
from grabcube import ImageGrab
class WebCamPointing:
    def __init__(self):
        self.grabber = ImageGrab(300)
        self.t1 = Telescope(3, '/dev/ttyUSB0')

        return None
    def single_grab(self):
        # open video0  cv2.CAP_V4L2
        cap = cv2.VideoCapture(0, cv2.CAP_V4L)
        # cap.set(cv2.CAP_PROP_FPS, 30.0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        codec = 0x47504A4D  # MJPG
        cap.set(cv2.CAP_PROP_FOURCC, codec)
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)  ) # float `width`
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  )# float `height`
        # print(cap.get(cv2.CAP_PROP_FPS))
        # The control range can be viewed through v4l2-ctl -L
        # full moon
        #print(condition)
        cap.set(cv2.CAP_PROP_BRIGHTNESS, 30)
        cap.set(cv2.CAP_PROP_CONTRAST, 32)
        cap.set(cv2.CAP_PROP_SATURATION, 128)
        cap.set(cv2.CAP_PROP_HUE, 40)
        cap.set(cv2.CAP_PROP_BACKLIGHT, 2)
        cap.set(cv2.CAP_PROP_GAIN, 30)
        cap.set(cv2.CAP_PROP_GAMMA, 200)
        cap.set(cv2.CAP_PROP_WB_TEMPERATURE, 2600)
        cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 3)
        cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
        cap.set(cv2.CAP_PROP_EXPOSURE, 5000)
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("Webcam_image.png", gray)
        time.sleep(1)
        ii2 = Image.open('Webcam_image.png')
        a = numpy.array(ii2)  # convert to array
        n, centroid_x, centroid_y = self.starfind_method3(a)
        #cv2.imwrite("Webcam_image.png", frame)
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

        
    def capture_and_findstar(self,center_try):
        # to check menus avaialable v4l2-ctl -L -d /dev/video2
        '''
        brightness 0x00980900 (int)    : min=-64 max=64 step=1 default=0 value=64
                               contrast 0x00980901 (int)    : min=0 max=64 step=1 default=32 value=0
                             saturation 0x00980902 (int)    : min=0 max=128 step=1 default=64 value=64
                                    hue 0x00980903 (int)    : min=-40 max=40 step=1 default=0 value=0
         white_balance_temperature_auto 0x0098090c (bool)   : default=1 value=1
                                  gamma 0x00980910 (int)    : min=72 max=500 step=1 default=100 value=100
                                   gain 0x00980913 (int)    : min=0 max=100 step=1 default=0 value=0
                   power_line_frequency 0x00980918 (menu)   : min=0 max=2 default=1 value=1
                        0: Disabled
                        1: 50 Hz
                        2: 60 Hz
              white_balance_temperature 0x0098091a (int)    : min=2800 max=6500 step=1 default=4600 value=4600 flags=inactive
                              sharpness 0x0098091b (int)    : min=0 max=6 step=1 default=3 value=3
                 backlight_compensation 0x0098091c (int)    : min=0 max=2 step=1 default=1 value=1
                          exposure_auto 0x009a0901 (menu)   : min=0 max=3 default=3 value=1
                        1: Manual Mode
                        3: Aperture Priority Mode
                      exposure_absolute 0x009a0902 (int)    : min=1 max=5000 step=1 default=156 value=5000
                 exposure_auto_priority 0x009a0903 (bool)   : default=0 value=0
        '''
      
        # open video0  cv2.CAP_V4L2
        cap = cv2.VideoCapture(0, cv2.CAP_V4L)
        # cap.set(cv2.CAP_PROP_FPS, 30.0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        codec = 0x47504A4D  # MJPG
        cap.set(cv2.CAP_PROP_FOURCC, codec)
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)  ) # float `width`
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  )# float `height`
        # print(cap.get(cv2.CAP_PROP_FPS))
        # The control range can be viewed through v4l2-ctl -L
        # full moon
        #print(condition)
        cap.set(cv2.CAP_PROP_BRIGHTNESS, 30)
        cap.set(cv2.CAP_PROP_CONTRAST, 32)
        cap.set(cv2.CAP_PROP_SATURATION, 128)
        cap.set(cv2.CAP_PROP_HUE, 40)
        cap.set(cv2.CAP_PROP_BACKLIGHT, 2)
        cap.set(cv2.CAP_PROP_GAIN, 30)
        cap.set(cv2.CAP_PROP_GAMMA, 200)
        cap.set(cv2.CAP_PROP_WB_TEMPERATURE, 2600)
        cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 3)
        cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
        cap.set(cv2.CAP_PROP_EXPOSURE, 5000)
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("Webcam_image.png", gray)
        #cv2.imwrite("Webcam_image.png", frame)
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        
        ii2 = Image.open('Webcam_image.png')
        a = numpy.array(ii2)  # convert to array
        n, centroid_x,centroid_y = self.starfind_method3(a)
        #print(n,centroid_x,centroid_y)
        #n, centroid_x, centroid_y = self.starfind_method1_webcam(a)
        print(n, centroid_x, centroid_y)

        # conversion numpy array into rgb image to show
        #c = cv2.cvtColor(image_read, cv2.COLOR_BGR2RGB)
        # cv2.namedWindow(file, cv2.WINDOW_KEEPRATIO)
        #imS = cv2.resize(image_read, (960, 540))  # Resize image
        #cv2.imshow('Webcam_image.JPG', imS)
        #cv2.imwrite("Pointing_Image1.jpg", imS)
        #k = cv2.waitKey(1000)
        # destroy the window
        #cv2.destroyAllWindows()
        if (n==1):
            xcenter = 380.39
            ycenter = 261.99        #260 # print(width,height,arrcX[indexofbright],arrcY[indexofbright])

            #265
            # Pixel Scale of arducam=

            if(center_try<=6):
                distance_from_center_x = (xcenter - centroid_x) * 0.004
                distance_from_center_y = (ycenter - centroid_y) * 0.004
                #print("fdasfdsfdsfdsf:", xcenter - centroid_x)
                if(((centroid_x - xcenter)< 1 and (centroid_y - ycenter) <1 and ((centroid_x - xcenter)>-1 and (centroid_y - ycenter) >-1))):
                    return 100


                print("Distance from center in deg.", distance_from_center_x, distance_from_center_y)
                self.t1.setSpeed(2)
                self.t1.setPointRate()
                #time.sleep(2)
                movetimeX = distance_from_center_x / 0.04
                movetimeY = distance_from_center_y / 0.04
                print("FASTTTTTTTT,Giving Offset to Meade for time (s): ", movetimeX, movetimeY)
            elif(center_try>6):
                distance_from_center_x = (xcenter - centroid_x) * 0.004
                distance_from_center_y = (ycenter - centroid_y) * 0.004
                if (((centroid_x - xcenter) < 1 and (centroid_y - ycenter) < 1 and (
                        (centroid_x - xcenter) > -1 and (centroid_y - ycenter) > -1))):
                    return 100
                print("Distance from center in deg.", distance_from_center_x, distance_from_center_y)
                self.t1.setSpeed(2)
                self.t1.setPointRateSlow()
                # time.sleep(2)
                movetimeX = distance_from_center_x / 0.01
                movetimeY = distance_from_center_y / 0.01
                print("SLOWWWWWWWWW,Giving Offset to Meade for time (s): ", movetimeX, movetimeY)

            if (movetimeY < 0):
                self.t1.telescopeMoveSouth(abs(movetimeY))
            elif (movetimeY > 0):
                self.t1.telescopeMoveNorth(abs(movetimeY))
            if (movetimeX < 0):
                self.t1.telescopeMoveWest(abs(movetimeX))
            elif (movetimeX > 0):
                self.t1.telescopeMoveEast(abs(movetimeX))
            return 1
        else:
            #No star found
            return -1
    def single_imager(self):
        self.grabber.single_image()
    def main_pointing_check(self):
        ii2 = Image.open('Main_Single_image.png')
        a = numpy.array(ii2)  # convert to array
        n= self.starfind_method1_main(a)

        if (n == 2):
            return 1
        else:
            return -1
    def starfind_webcam(self,data):
        mean, median, std = sigma_clipped_stats(data, sigma=3.0)
        starfind = IRAFStarFinder(fwhm=6.0, threshold=60.0, sharplo=-10.0, sharphi=10.0, roundlo=-10.0, roundhi=10.0)
        sources = starfind(data - median)
        centroids = []
        fwhm = []
        sharpness = []
        roundness = []
        peak_count = []
        if (str(type(sources)) != "<class 'NoneType'>"):
            n = len(sources)
            if (n == 1):
                for i in range(n):
                    centroids.append([float(sources[i]['xcentroid']), float(sources[i]['ycentroid'])])
                    fwhm.append(float(sources[i]['fwhm']))
                    sharpness.append(float(sources[i]['sharpness']))
                    roundness.append(float(sources[i]['roundness']))
                    # peak_count.append(float(sources[i]['sky'])+float(sources[i]['peak']))
                    peak_count.append(float(sources[i]['peak']))
                if (centroids[0][0] > centroids[1][0]):
                    centroids = [[centroids[1][0], centroids[1][1]], [centroids[0][0], centroids[0][1]]]
                    fwhm = [fwhm[1], fwhm[0]]
                    sharpness = [sharpness[1], sharpness[0]]
                    roundness = [roundness[1], roundness[0]]
                    peak_count = [peak_count[1], peak_count[0]]
            else:
                n = -1
                centroids = [[0, 0], [0, 0]]
                fwhm = [0, 0]
                sharpness = [0, 0]
                roundness = [0, 0]
                peak_count = [0, 0]
        else:
            n = 0
            centroids = [[0, 0], [0, 0]]
            fwhm = [0, 0]
            sharpness = [0, 0]
            roundness = [0, 0]
            peak_count = [0, 0]
        return n, centroids


    def starfind_method1_main2(self,data):
        mean, median, std = sigma_clipped_stats(data, sigma=3.0)
        #print((mean, median, std))
        starfind = IRAFStarFinder(fwhm=6.0, threshold=600.0, sharplo=-10.0, sharphi=10.0, roundlo=-10.0, roundhi=10.0)
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
                    #peak_count.append(float(sources[i]['sky'])+float(sources[i]['peak']))
                    peak_count.append(float(sources[i]['peak']))
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
        return n,  centroids
    def starfind_method1_main(self,data):
        mean = np.mean(data)
        sig = np.std(data)
        smooth = nd.gaussian_filter(data, 3.0)
        # print(sig)
        clip_data = smooth >= (mean + 50.0)
        clip = clip_data
        labels, num = nd.label(clip)
        pos = nd.center_of_mass(data, labels, range(num + 1))
        print(num)
        centroids = pos[1:]
        print(centroids)
        if (num == 2):
            x1 = centroids[0][1]
            y1 = centroids[0][0]
            x2 = centroids[1][1]
            y2 = centroids[1][0]
            print("x1,y1,x2,y2", x1, y1, x2, y2)
            centroids = [[x1, y1], [x2, y2]]
            if (float(x1) > float(x2)):
                # print("\n \n \n Star 2 found before Star1, rearranging")
                centroids = [[x2, y2], [x1, y1]]
                # print("\n \n \n Rearranged", centroids)

            fwhm = [0, 0]
            sharpness = [0, 0]
            roundness = [0, 0]
            peak_count = [0, 0]
        else:
            centroids = [[0, 0], [0, 0]]
            num = 0
            fwhm = [0, 0]
            sharpness = [0, 0]
            roundness = [0, 0]
            peak_count = [0, 0]
        return num, centroids

    def starfind_method2(self,data):
        mean = np.mean(data)
        sig = np.std(data)
        smooth = nd.gaussian_filter(data, 3.0)
        # print(mean)
        clip_data = smooth >= (mean + 20.0)
        clip = clip_data
        labels, num = nd.label(clip)
        pos = nd.center_of_mass(data, labels, range(num + 1))
        centroids = pos[1:]
        '''
        brightness= []
        for item in centroids:
            #print(item)
            brightness.append(item[2])
        #height = data.shape[0]
        #width = data.shape[1]
        '''
        if num==0:
            return 0, 0, 0
        #bb_index=brightness.index(min(brightness))
        bb_index=0
        print(num,centroids[bb_index][1], centroids[bb_index][0])
        
        positions = np.transpose((int(centroids[bb_index][1]), int(centroids[bb_index][0])))
        apertures = CircularAperture(positions, r=7.)
        norm = ImageNormalize(stretch=SqrtStretch())
        plt.figure(figsize=(8, 4))
        plt.imshow(data, cmap='Greys', origin='lower', norm=norm, interpolation='nearest')
        plt.imshow(data, origin='lower', interpolation='nearest')
        plt.scatter(int(centroids[bb_index][1]), int(centroids[bb_index][0]), marker='+', s=30, color='red')
        apertures.plot(color='blue', lw=1.5, alpha=0.5)
        plt.savefig('Webcam_star_detect.png')
        return 1, centroids[bb_index][1], centroids[bb_index][0]

    def starfind_method3(self, data):
        import cv2
        import numpy as np;

        # apply a Gaussian blur to the image then find the brightest
        # region
        gray = cv2.GaussianBlur(data, (5, 5), 0)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
        #print(maxLoc, minVal, maxVal)

        cv2.circle(data, maxLoc, 5, (0, 0, 255), 2)
        # display the results of our newly improved method
        # cv2.imshow("Robust", image)
        # cv2.waitKey(0)
        cv2.imwrite("Webcam_star_detect.png", data)

        return 1, maxLoc[0], maxLoc[1]

def main():
    print("-----------Webcam Pointing---------")
    webpoint = WebCamPointing()
    centering = 1
    ret=webpoint.capture_and_findstar(centering)
    try_count=0
    while(centering<10):
        centering+=1
        print("Centering run: ",centering)
        ret=webpoint.capture_and_findstar(centering)
        if(ret==100):
            print("Automated pointing done")
            break
        #time.sleep(1)
    '''    
    while(1):
        if(ret==1):
            print("Star Centered in Webcam..Checking now in Main..")
            webpoint.single_imager()
            time.sleep(2)
            ret1=webpoint.main_pointing_check()
            if(ret1==1):
                print("Star Found in Main...Start DIMM...")
                break
            else:
                try_count += 1
                print("Not found in MAIN, Retrying")
                ret = webpoint.capture_and_findstar()
                if (try_count == 10):
                    print("Unable to find star in 10 try, Exiting the search...Look manually...")
                    break

        else:
            try_count+=1
            print("Not found in WEBCAM, Retrying")
            ret = webpoint.capture_and_findstar()
            if(try_count==10):
                print("Unable to find star in 10 try, Exiting the search...Look manually...")
                break
    '''
    # pass
if __name__ == "__main__":
    main()
