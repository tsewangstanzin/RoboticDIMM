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
        
        
        return None
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
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 648)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 490)
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

    def starfind_method1_webcam(self,data):
        mean, median, std = sigma_clipped_stats(data, sigma=3.0)
        starfind = IRAFStarFinder(fwhm=10.0, threshold=100. * std, sigma_radius=1.5, minsep_fwhm=2.0, sharplo=-100.0,
                                  sharphi=100.0, roundlo=-100.0, roundhi=100.0, sky=None, exclude_border=False,
                                  brightest=1, peakmax=None)
        sources = starfind(data - median)
        print((sources))
        if (str(type(sources)) != "<class 'NoneType'>"):
            n = len(sources)
            centroids = []
            if (n == 1):
                for i in range(n):
                    centroids.append([float(sources[i]['xcentroid']), float(sources[i]['ycentroid'])])

                positions = np.transpose((sources['xcentroid'], sources['ycentroid']))
                apertures = CircularAperture(positions, r=4.)
                norm = ImageNormalize(stretch=SqrtStretch())
                # plt.imshow(data, cmap='Greys', origin='lower', norm=norm,interpolation='nearest')
                # plt.show()
                # This condition below is important as sometimes the algorithm find STAR2 earlier than STAR1
                # messing the x1,y1 and x2,y2 array
                # print("Centroiding layer 1:")
                # print(centroids)
                # data = make_4gaussians_image()
                x_init = (int(centroids[0][0]))
                y_init = (int(centroids[0][1]))
                # Functions avaialable: centroid_2dg() centroid_1dg() centroid_quadratic() centroid_com()
                x, y = centroid_sources(data, x_init, y_init, box_size=21, centroid_func=centroid_com)
                # print("Centroiding layer 2:")
                centroids = [[x[0], y[0]]]

                plt.figure(figsize=(8, 4))

                plt.imshow(data, cmap='Greys', origin='lower', norm=norm, interpolation='nearest')
                plt.imshow(data, origin='lower', interpolation='nearest')
                plt.scatter(x, y, marker='+', s=30, color='red')

                apertures.plot(color='blue', lw=1.5, alpha=0.5)
                plt.savefig('Webcam_star_detect.png')
                # plt.tight_layout()
                # plt.show(block=False)
                # plt.pause(3)
                # plt.close()
            else:
                n = 2
                centroids =[ [0, 0]]
        else:
            n = 0
            centroids = [[0, 0]]

        return n,  centroids[0][0], centroids[0][1]
    def starfind_method1_main(self,data):
        mean, median, std = sigma_clipped_stats(data, sigma=3.0)
        starfind = IRAFStarFinder(fwhm=3.0, threshold=10. * std, sigma_radius=1.5, minsep_fwhm=2.0, sharplo=-10.0,
                                  sharphi=10.0, roundlo=-10.0, roundhi=10.0, sky=None, exclude_border=False,
                                  brightest=None, peakmax=None)

        sources = starfind(data - median)
        print((sources))
        if (str(type(sources)) != "<class 'NoneType'>"):
            n = len(sources)
            centroids = []
            if (n == 2):
                for i in range(n):
                    centroids.append([float(sources[i]['xcentroid']), float(sources[i]['ycentroid'])])

                positions = np.transpose((sources['xcentroid'], sources['ycentroid']))
                apertures = CircularAperture(positions, r=4.)
                norm = ImageNormalize(stretch=SqrtStretch())
                # plt.imshow(data, cmap='Greys', origin='lower', norm=norm,interpolation='nearest')
                # plt.show()
                # This condition below is important as sometimes the algorithm find STAR2 earlier than STAR1
                # messing the x1,y1 and x2,y2 array
                # print("Centroiding layer 1:")
                # print(centroids)
                # data = make_4gaussians_image()
                x_init = (int(centroids[0][0]))
                y_init = (int(centroids[0][1]))
                # Functions avaialable: centroid_2dg() centroid_1dg() centroid_quadratic() centroid_com()
                x, y = centroid_sources(data, x_init, y_init, box_size=21, centroid_func=centroid_com)
                # print("Centroiding layer 2:")
                centroids = [[x[0], y[0]]]

                plt.figure(figsize=(8, 4))

                plt.imshow(data, cmap='Greys', origin='lower', norm=norm, interpolation='nearest')
                plt.imshow(data, origin='lower', interpolation='nearest')
                plt.scatter(x, y, marker='+', s=30, color='red')

                apertures.plot(color='blue', lw=1.5, alpha=0.5)
                plt.savefig('Main_star_detect.png')
                # plt.tight_layout()
                # plt.show(block=False)
                # plt.pause(3)
                # plt.close()
            else:
                n = 1
                centroids = [0, 0]
        else:
            n = 0
            centroids = [0, 0]

        return n
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
        # print(pos)
        #print(centroids)
        #height = data.shape[0]
        #width = data.shape[1]
        if num==0:
            return 0, 0, 0
        print(num,centroids[0][1], centroids[0][0])
        return 1, centroids[0][1], centroids[0][0]

def main():
    print("-----------Webcam Imaging---------")
    webpoint = WebCamPointing()
    centering = 1
    ret=webpoint.capture_and_findstar(centering)
    try_count=0
    while(centering<=5):
       
        print("Clearing run: ",centering)
        centering+=1
        ret=webpoint.capture_and_findstar(centering)
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
