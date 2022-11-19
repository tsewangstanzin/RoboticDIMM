'''
Integration of all in one for robotic operation
Created Nov 2021
@author Tsewang Stanzin, IIA-IAO Hanle
'''
#Custom code imports:
from grabcube import ImageGrab
from seeing_analysis_v1 import Seeing
from meade_tel_control import Telescope
import best_stars
import auto_plotter_transfer
#Python library imports:
import numpy as np
import datetime
import ephem
import time
from datetime import datetime, timedelta
import sys,select,os
import shutil
import re

class Observation:
    def __init__(self):
        ret=self.start_obs()
        if(ret==1):
            self.grabber = ImageGrab(300)
            self.t1 = Telescope(3, '/dev/ttyUSB0')
            print("Updating Meade GPS, please wait for 1min.")
            self.t1.setGPS()
            time.sleep(60)
            #Toggle to set precision to high
            telRA=self.t1.getTelRA()
            if(len(telRA)==8):
                self.t1.setPrecision()
                print("Meade Changed to High Precision mode")
            else:
                print("Meade aready in High Precision mode")
        self.WorkingDir=None
        self.tel_alt=0.0

        self.airmass=0.0
        self.obj_ra = ''
        self.obj_dec = ''
        self.good = []

        self.cloud=False
        self.light_status=False
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
    def findandslew_stars(self):
        iao = best_stars.iao_site()
        cat_visible = best_stars.hr_catalog(iao)

        el_limit = 40.0 * ephem.pi / 180.0
        #az_limit = 1.0 * ephem.pi / 180.0
        self.good = []

        for key, star in cat_visible.items():
            dec = float(star.dec) * 180.0 / np.pi
            if star.alt > el_limit and dec > 0.0 and dec < 50.0:
                self.good.append(key)
        sorted_good= []
        for x in self.good:
            a=float(cat_visible[x].alt)
            sorted_good.append([x,a])
        sorted_good.sort(key=lambda x: x[1])
        #sorted_good.sort(key = lambda x: x[1],reverse=True)
        self.good=[]
        for x in sorted_good:
            self.good.append(x[0])


        if (len(self.good) > 0):
            for s in self.good:

                iao.date = ephem.now()
                star = cat_visible[s]
                star.compute(iao)
                lst = iao.sidereal_time()
                ha = ephem.hours(lst - star.ra)
                if star.alt > 0.0:
                    self.airmass = 1 / np.cos(ephem.degrees('90:00:00') - star.alt)
                else:
                    self.airmass = 999.0
                print(
                    "Name= %s; C_RA= %s; C_DEC= %s; A_RA= %s; A_DEC= %s; Mag= %f; AMass= %f;  HA = %s;  LST= %s; Alt = %s;  Az = %s" % (
                        star.name, star.a_ra, star.a_dec, star.ra, star.dec, star.mag, self.airmass, ha, lst, star.alt,
                        star.az))

            print("\nPointing to best one: ")
            iao.date = ephem.now()
            star1 = cat_visible[self.good[0]]
            star1.compute(iao)
            lst = iao.sidereal_time()
            ha = ephem.hours(lst - star1.ra)
            if star1.alt > 0.0:
                self.airmass = 1 / np.cos(ephem.degrees('90:00:00') - star1.alt)
            else:
                self.airmass = 999.0
            print(
                "Name= %s; C_RA= %s; C_DEC= %s; A_RA= %s; A_DEC= %s; Mag= %f; AMass= %f;  HA = %s;  LST= %s; Alt = %s;  Az = %s" % (
                    star1.name, star1.a_ra, star1.a_dec, star1.ra, star1.dec, star1.mag, self.airmass, ha, lst, star1.alt, star1.az))

            self.obj_ra= star1.a_ra
            self.obj_dec= star1.a_dec

            hms = str(star1.ra)
            hms = hms.split(":")
            h = hms[0]
            m = hms[1]
            s = hms[2].split('.')
            s = s[0]

            sdms = str(star1.dec)
            sdms = sdms.split(":")
            mi = sdms[1]
            se = sdms[2].split('.')
            se = se[0]
            deint = int(sdms[0])
            if (deint > 0):
                sign = '+'
                de = sdms[0]
            else:
                sign = '-'
                de = sdms[0].split('-')
                de = de[0]
            
            # Meade control
            Meadetime = self.t1.gettelescopeTime()
            print("Meade Telescope time IST: ", Meadetime.decode('utf-8'))
            # time.sleep(10)
            self.t1.setSpeed(3)
            slew_flag = self.t1.RADECPointing(h, m, s, sign, de, mi, se)
            #slew_flag = self.t1.RADECPointing('13', '35', '2', '+', '48', '48', '3')
            if (slew_flag.decode('latin-1') == '0'):
                print("Meade accepted the slew command")
            else:
                print("Out of Limit")
                return 0, False
            sr = self.t1.getSlewStatus()
            distance_bars = len(sr)
            while (distance_bars != 1):
                sr = self.t1.getSlewStatus()
                distance_bars = len(sr)
                print("Telescope slewing...")
            


            slew_done = True
            return self.good[0],slew_done
        else:
            return 0,False
    def start_obs(self):
        ret=best_stars.night_start()
        return ret
    def dimmrun(self):
        #Calculate Star Airmass
        # Pointing Done, Telescope is Tracking, No need to point just fetch star position
        iao = best_stars.iao_site()
        iao.date = ephem.now()
        star1 = ephem.FixedBody()
        star1._ra = self.obj_ra
        star1._dec = self.obj_dec
        star1._epoch = ephem.J2000
        star1.compute(iao)
        lst = iao.sidereal_time()
        ha = ephem.hours(lst - star1.ra)
        self.airmass = 1 / np.cos(ephem.degrees('90:00:00') - star1.alt)
        #print("Current Target Name: %s Az: %.3f El: %.3f HA: " %(star1.name, star1.az, star1.alt))
        # Read telescope Altitude from Meade while tracking
        alt = self.t1.getTelAlt()
        alt = alt.decode('latin-1')
        alt_dms = re.split('[ß : #]', alt)
        if (float(alt_dms[0]) < 0):
            self.tel_alt = float(alt_dms[0]) - float(alt_dms[1]) / 60 - float(alt_dms[2]) / (60 * 60)
        else:
            self.tel_alt = float(alt_dms[0]) + float(alt_dms[1]) / 60 + float(alt_dms[2]) / (60 * 60)


        ret_3D_array,fits_file_name = self.grabber.create_cube(self.WorkingDir)
        #Flat field correction to be put here


        analyser = Seeing(ret_3D_array,fits_file_name)
        x2, y2, x1, y1, c1, c2, d1, d2, starnotfound, last_c1, last_c2, fwhm1, sharpness1, roundness1, peak_count1,fwhm2, sharpness2, roundness2, peak_count2,cent_filename = analyser.compute(self.WorkingDir)
        now = datetime.now()
        f2 = open(str(self.WorkingDir) + '/Seeing_Tokovin.dat', 'a')
        f3 = open(str(self.WorkingDir) + '/Seeing_Fried.dat', 'a')
        if (os.stat(str(self.WorkingDir) + '/Seeing_Tokovin.dat').st_size == 0):
            f2.write("#CENTFILE DATE TIME VAR_X VAR_Y MEAN_CENTER_X MEAN_CENTER_Y MEAN_INTENSITY_1 MEAN_INTENSITY_1 REJECTED_STARS MEAN_FWHM_1 MEAN_FWHM_2 MEAN_SHARPNESS_1 MEAN_SHARPNESS_2 MEAN_ROUNDNESS_1 MEAN_ROUNDNESS_2 MEAN_PEAK_1 MEAN_PEAK_2 SEEING_X SEEING_Y RA DEC AZ Alt Airmass\n")
        if (os.stat(str(self.WorkingDir) + '/Seeing_Fried.dat').st_size == 0):
            f3.write("#CENTFILE DATE TIME VAR_X VAR_Y MEAN_CENTER_X MEAN_CENTER_Y MEAN_INTENSITY_1 MEAN_INTENSITY_1 REJECTED_STARS MEAN_FWHM_1 MEAN_FWHM_2 MEAN_SHARPNESS_1 MEAN_SHARPNESS_2 MEAN_ROUNDNESS_1 MEAN_ROUNDNESS_2 MEAN_PEAK_1 MEAN_PEAK_2 SEEING_X SEEING_Y RA DEC Az Alt Airmass\n")
        if (starnotfound < 150):
            self.cloud = False
            # Variance over x and y axis
            varx = np.var(np.sqrt(abs(x2 - x1) ** 2))
            vary = np.var(np.sqrt(abs(y2 - y1) ** 2))
            # Combined variance
            r = np.sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
            var = np.var(r)
            print("VarX = %f, VarY = %f, Combined vAr= %f"% (varx, vary,var))
            # Seeing Method 1 tokovin
            seeing_x_saravin = float(analyser.seeing_saravin_x(varx))
            seeing_y_saravin = float(analyser.seeing_saravin_y(vary))
            print("Saravin:  Seeing X = %f, Seeing Y = %f" % (seeing_x_saravin, seeing_y_saravin))
            f2.write("%s %s %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %s %s %f %f %f\n" % (
                cent_filename,now, varx, vary, np.mean(c1), np.mean(c2), np.mean(d1), np.mean(d2),starnotfound, np.mean(fwhm1), np.mean(fwhm2),
                np.mean(sharpness1),np.mean(sharpness2), np.mean(roundness1), np.mean(roundness2),  np.mean(peak_count1),
                np.mean(peak_count2), seeing_x_saravin, seeing_y_saravin, self.obj_ra,self.obj_dec,float(star1.az) * 180.0 / np.pi,float(star1.alt) * 180.0 / np.pi, self.airmass))
            #Star Related self.ra, self.dec, self.airmass,seeing_x_saravn with Airmass correction  tel_alt
            # Seeing Method 1 Saravin
            seeing_x_fried = float(analyser.seeing_fried_x(varx))
            seeing_y_fried = float(analyser.seeing_fried_y(vary))
            print("Fried:  Seeing X = %f, Seeing Y = %f" % (seeing_x_fried, seeing_y_fried))
            f3.write("%s %s %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %s %s %f %f %f\n" % (
                cent_filename,now, varx, vary, np.mean(c1), np.mean(c2), np.mean(d1), np.mean(d2),starnotfound, np.mean(fwhm1), np.mean(fwhm2),
                np.mean(sharpness1),np.mean(sharpness2), np.mean(roundness1), np.mean(roundness2), np.mean(peak_count1),
                np.mean(peak_count2),  seeing_x_fried,
                seeing_y_fried,self.obj_ra,self.obj_dec,float(star1.az) * 180.0 / np.pi,float(star1.alt) * 180.0 / np.pi, self.airmass))

            print("\n Giving Guide Offset")

            self.t1.setGuideRate()
            current_star_x = last_c1
            current_star_y = last_c2
            #Basler
            #distance_from_center_x = (329.5 - current_star_x) * 0.50077
            #distance_from_center_y = (247 - current_star_y) * 0.50077

            #CMOS  3by3 binning
            distance_from_center_x = (200.0 - current_star_x) * 0.46692
            distance_from_center_y = (200.0 - current_star_y) * 0.46692

            movetimeX = distance_from_center_x / 15.0
            movetimeY = distance_from_center_y / 15.0
            print(current_star_x, current_star_y, distance_from_center_x, distance_from_center_y, movetimeX,
                  movetimeY)
            if (movetimeY < 0):
                self.t1.telescopeMoveSouth(abs(movetimeY))
            elif (movetimeY > 0):
                self.t1.telescopeMoveNorth(abs(movetimeY))
            if (movetimeX > 0):
                self.t1.telescopeMoveWest(abs(movetimeX))
            elif (movetimeX < 0):
                self.t1.telescopeMoveEast(abs(movetimeX))

            #print("Time taken to find centroids and compute seeing from 300 full frame 16bit image: %.3f"%(end - start))
            
        else:
            print("\n")
            print("Seems its cloudy, Changing target....")
            #self.cloud = True
        
        f2.close()
        f3.close()
        #Check for Light/Sun ,No light sensor needed
        self.light_status = self.start_obs()
        return self.tel_alt,self.cloud,self.light_status

    def close_port(self):
        self.t1.ser.close()
    def single_imager(self):
        self.grabber.single_image()


if __name__ == '__main__':
    obs = Observation()
    WD = obs.working_directory()
    print("Working Directory : %s UTC Date and time: %s"%(WD,datetime.now()))
    if (os.path.exists(WD)):
        print("Script restarted in between observation, Continuing with the scheduler.......")
    if not os.path.exists(WD):
        os.mkdir(WD)
        # Load Star Catalog, do not load the full catalog if script is stopped in between observation
        sourcePath = "starcatalog.lst"
        destinationPath = "scheduler_star.lst"
        shutil.copyfile(sourcePath, destinationPath)

    #Main Loop between Day and Night
    while(True):
        ret_night=obs.start_obs()
        #Internal Loop for night
        findandslew_flag = True
        while(ret_night==True):
            ret_night = obs.start_obs()
            if(ret_night==False):
                break
            if(findandslew_flag==True):
                name,slew_done=obs.findandslew_stars()
                if(slew_done):
                    print("Telescope Slew Complete")
                    findandslew_flag == False
                if(name==0):
                    print("No star found OR Exception Slew error, Attend pointing manually ")
                if(name!=0):
                    fp = open("scheduler_star.lst", "r")
                    lines = fp.readlines()
                    fp.close()
                    visitedstar=open(str(WD)+"/visitedstar.lst", "a")
                    if (os.stat(str(WD)+"/visitedstar.lst").st_size == 0):
                        visitedstar.write("# Line# RA           DEC         Epoch    RA     DEC   MAG    Title   Comments:\n")
                        visitedstar.write("# HR#                                     PM     PM           HD #    Spec    Cross-ref    R-Velocity \n")
                    with open("scheduler_star.lst", 'w') as file:
                        for line in lines:
                            # find() returns -1 if no match is found
                            if  line[1:5].strip()==name:
                                visitedstar.write(line)
                                pass
                            else:
                                file.write(line)
                    visitedstar.close()
                    file.close()

            i = 0
            #This will get removed when auto pointing from webcam is done
            while (1):
                obs.single_imager()
                '''
                from webcam_pointing_v2 import WebCamPointing
                centering = 1
                ret = WebCamPointing.capture_and_findstar(centering)
                try_count = 0
                while (centering < 10):
                    centering += 1
                    print("Centering run: ", centering)
                    ret = WebCamPointing.capture_and_findstar(centering)
                '''
                print(str("Pointing Algorithm: HUMAN INTERVENTION NEEDED....Manually offset from webcam and press ENTER when star centered.Check:")+str(i+1), end = "\r")
                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    line = input()
                    break
                i += 1
                time.sleep(1)
            while (1):
                tel_alt,cloud,light_status=obs.dimmrun()
                print("Telescope Altitude (Tracking):  %.4f" %(tel_alt))
                print("Cloud Status: " ,cloud)
                print("Night Status: ", light_status)
                print("Rain: Unknown")
                print("Wind: Unknown")
                if(tel_alt<35.0 or tel_alt >80.0):
                    print("Changing the target star")
                    findandslew_flag = True
                    break
                else:
                    print("Keeping the target star")
                    findandslew_flag=False
                obs.single_imager()

            #obs.close_port()
            time.sleep(1)

        # Night Loop exit, time to plot the seeing, star plot,etc and transfer data through SFTP to Server PC at communication room
        auto_plotter_transfer.seeing_plot(WD)
        time.sleep(3)
        print("Transferring data....")
        #transfer_flag = auto_plotter_transfer.ssh_data_send(WD)
        transfer_flag=1
        if (transfer_flag == 1):
            print("Succesfull data transfer over SSH FTP")
        #Internal Loop for day
        while(ret_night==False):
            ret_night = obs.start_obs()
            if(ret_night==True):
                break
            time.sleep(1)

