import os
import pysftp
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import math,sys
import pathlib
import argparse
from slack_bot import Messenger
def progressbar(x, y):
    bar_len = 60
    filled_len = math.ceil(bar_len * x / float(y))
    percents = math.ceil(100.0 * x / float(y))
    bar = '#' * filled_len + '-' * (bar_len - filled_len)
    filesize = f'{math.ceil(y / 1024):,} KB' if y > 1024 else f'{y} byte'
    sys.stdout.write(f'[{bar}] {percents}% {filesize}\r')
    sys.stdout.flush()
def ssh_data_send(wdr):
    with pysftp.Connection('172.16.16.58', username='iaodata', password='iao-hanle-DatA',port=220) as sftp:
        wd = wdr
        if wd not in sftp.listdir('/C/xampp3/htdocs/IAO/sky/DIMM/'):
            sftp.mkdir(os.path.join('/C/xampp3/htdocs/IAO/sky/DIMM/', wd))
            with sftp.cd('/C/xampp3/htdocs/IAO/sky/DIMM/'):
                if 'Latest.png' in sftp.listdir('/C/xampp3/htdocs/IAO/sky/DIMM/'):
                    sftp.remove('/C/xampp3/htdocs/IAO/sky/DIMM/Latest.png')
                sftp.put("/home/iiap/" + wd + "/" + str(
                    wd) + "_seeingplot.png")
                sftp.rename('/C/xampp3/htdocs/IAO/sky/DIMM/' + str(wd) + '_seeingplot.png',
                            '/C/xampp3/htdocs/IAO/sky/DIMM/Latest.png')
            with sftp.cd('/C/xampp3/htdocs/IAO/sky/DIMM/' + wd):
                for file in os.listdir(wd):
                    if(pathlib.Path(file).suffix!='.fits'):
                    	print(str(file))
                    	sftp.put("/home/iiap/" + wd + "/" + str(file), callback=lambda x, y: progressbar(x, y))
                    print('\n')
            return 1
        else:
            with sftp.cd('/C/xampp3/htdocs/IAO/sky/DIMM/'):
                if 'Latest.png' in sftp.listdir('/C/xampp3/htdocs/IAO/sky/DIMM/'):
                    sftp.remove('/C/xampp3/htdocs/IAO/sky/DIMM/Latest.png')
                sftp.put("/home/iiap/" + wd + "/" + str(wd)+"_seeingplot.png")  # upload file to allcode/pycode on remote
                sftp.rename('/C/xampp3/htdocs/IAO/sky/DIMM/'+str(wd)+'_seeingplot.png','/C/xampp3/htdocs/IAO/sky/DIMM/Latest.png')
            with sftp.cd('/C/xampp3/htdocs/IAO/sky/DIMM/'+wd):
                for file in os.listdir(wd):
                    
                    #sftp.put("/home/iiap/"+wd+"/"+str(file))
                    if(pathlib.Path(file).suffix!='.fits'):
                    	print(str(file))
                    	sftp.put("/home/iiap/" + wd + "/" + str(file), callback=lambda x, y: progressbar(x, y))
                    print('\n')
            return 1
def seeing_plot(wdr):
    filename = "/home/iiap/"+str(wdr)+'/Seeing_Tokovin.dat' #This is simply a string of text
    filename2 = "/home/iiap/" + str(wdr) + '/Seeing_Fried.dat'  # This is simply a string of text
    if (os.path.exists(filename)):
        array_from_file = np.loadtxt(filename, dtype=str,comments='#')
        array_from_file2 = np.loadtxt(filename2, dtype=str,comments='#')
        x = array_from_file[:, 18]
        y=  array_from_file[:, 19]
        time_raw=array_from_file[:,2]

        x2 = array_from_file2[:, 18]
        y2 = array_from_file2[:, 19]
        time2_raw = array_from_file2[:, 2]
        seeing_x_raw = x.astype(float)
        seeing_y_raw=  y.astype(float)
        seeing_x2_raw = x2.astype(float)
        seeing_y2_raw = y2.astype(float)
        seeing_x=[]
        seeing_y=[]
        seeing_x2=[]
        seeing_y2=[]
        time=[]
        time2=[]
        for i in range (len(seeing_x_raw)): 	
        	if seeing_x_raw[i]<5.0:
        		seeing_x.append(seeing_x_raw[i])
        		seeing_y.append(seeing_y_raw[i])
        		time.append(time_raw[i])
        		time2.append(time2_raw[i])

        plt.figure(figsize=(14, 8), num='Seeing Plot')
        median_see_xf=np.median(np.append(seeing_x, seeing_x2))
        median_see_yf=np.median(np.append(seeing_y, seeing_y2))
        plt.title('Atmospheric Seeing '+str(wdr)+'  Median Seeing Long.: '+str("%.4f"%median_see_xf)  + '"  Median Seeing Trav.: '+str("%.4f"%median_see_yf+'"'),size=10,weight="heavy",loc="center",color="Blue")
        plt.title("©IAO RoboDIMM", size=10,weight="heavy" ,loc='right',color="black")
        plt.xlabel("Time [UTC]",color="magenta",weight="heavy")
        plt.ylabel("Seeing [Arcseconds]",color="magenta",weight="heavy")
        timeArray = [datetime.datetime.strptime(i, '%H:%M:%S.%f') for i in time]
        timeArray2 = [datetime.datetime.strptime(i, '%H:%M:%S.%f') for i in time2]
        plt.plot([], [])
        plt.scatter(timeArray, seeing_x, color="blue", edgecolors="white", marker='P', linewidths=0.1, alpha=0.7,
                    label='Longitudenal', s=40)
        plt.scatter(timeArray, seeing_y, color="red", edgecolors="white", marker='X', linewidths=0.1, alpha=0.7,
                    label='Traversal', s=40)
        #plt.scatter(timeArray, seeing_x, color="orange", edgecolors="white", marker='^', linewidths=0.1, alpha=0.7,
        #            label='Longitudenal', s=30)
        #plt.scatter(timeArray, seeing_y, color="red", edgecolors="white", marker='o', linewidths=0.1, alpha=0.7,
        #            label='Traversal', s=30)
        #plt.scatter(timeArray2, seeing_x2,color="green", edgecolors="white", marker='X', linewidths=0.1, alpha=0.7,
        #            label='Longitudenal (Fried et.al)', s=30)
        #plt.scatter(timeArray2, seeing_y2, color="blue", edgecolors="white", marker='P', linewidths=0.1, alpha=0.7,
        #            label='Traversal (Fried et.al)', s=30)
        plt.legend()
        plt.gcf().autofmt_xdate()
        myFmt = mdates.DateFormatter('%H:%M')
        plt.gca().xaxis.set_major_formatter(myFmt)
        #plt.gcf().set_dpi(300)
        plt.savefig("/home/iiap/" + str(wdr) + "/" + str(wdr) + "_seeingplot.png")
        #plt.show()
        plt.close()
    else:
        plt.figure(figsize=(14, 8), num='Seeing Plot')
        plt.title('Atmospheric Seeing ' + str(wdr), size=10, weight="heavy",loc="center", color="Blue")
        plt.title("©IAO RoboDIMM", size=10, weight="heavy", loc='right', color="black")
        plt.text(0.6, 0.5, "No DIMM data for: "+str(wdr), ha="right", weight="heavy",color="red")
        plt.savefig("/home/iiap/" + str(wdr) + "/" + str(wdr) + "_seeingplot.png")
        #plt.show()
    print("Seeing plot generated")
    Messenger().txtmessage(str("Seeing Plot for: "+wdr))

    Messenger().filemessage(str("/home/iiap/" + str(wdr) + "/" + str(wdr) + "_seeingplot.png"))
def working_directory():
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
        WorkingDir = now.strftime("%Y%m%d")
    else:
        yesterday_date = date_today - timedelta(hours=24)
        yesterday_date = yesterday_date.strftime("%Y%m%d")
        WorkingDir = yesterday_date
    return WorkingDir
def main(wd):
    #wd=working_directory()
    seeing_plot(wd)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    d_wd=working_directory()
    parser.add_argument("-d",help="date",default=d_wd)
    args = parser.parse_args()
    print("Generated plot for: ",args.d)
    main(args.d)
