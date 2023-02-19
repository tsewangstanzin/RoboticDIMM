import os
import pysftp
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import math,sys
import pathlib
import argparse
import glob
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
    filename = str(wdr)+'/Seeing_Tokovin.dat' #This is simply a string of text
    filename2 = str(wdr) + '/Seeing_Fried.dat'  # This is simply a string of text
    if (os.path.exists(filename)):
        array_from_file = np.loadtxt(filename, dtype=str,comments='#')
        array_from_file2 = np.loadtxt(filename2, dtype=str,comments='#')
        x = array_from_file[:, 18]
        y=  array_from_file[:, 19]
        time_raw=array_from_file[:,2]
        date_raw = array_from_file[:, 1]

        x2 = array_from_file2[:, 18]
        y2 = array_from_file2[:, 19]
        time2_raw = array_from_file2[:, 2]
        date2_raw = array_from_file[:, 1]

        seeing_x_raw = x.astype(float)
        seeing_y_raw=  y.astype(float)
        seeing_x2_raw = x2.astype(float)
        seeing_y2_raw = y2.astype(float)
        seeing_x=[]
        seeing_y=[]
        seeing_x2=[]
        seeing_y2=[]

        dte=[]
        dte2 = []
        rejected_stars=array_from_file[:, 9].astype(float)
        altitudes_stars=array_from_file[:, 23].astype(float)
        
        
        for i in range (len(seeing_x_raw)):

            #We will strictly plot data which has zero rejected points
 
            zdeg=float(90.0)-float(altitudes_stars[i])
            za = (zdeg*np.pi)/180.0 # angle in rad
            zz=np.cos(za)**0.6
            diff=abs(seeing_x_raw[i]-seeing_y_raw[i])


            if seeing_x_raw[i]<4.0:
                seeing_x.append(seeing_x_raw[i]*zz)
                seeing_y.append(seeing_y_raw[i]*zz)
                dte.append(str(date_raw[i])+" "+str(time_raw[i]))
                dte2.append(str(date2_raw[i]) + " " + str(time2_raw[i]))

        plt.figure(figsize=(14, 8), num='Seeing Plot')
        #median_see_xf=np.median(np.append(seeing_x, seeing_x2))
        #median_see_yf=np.median(np.append(seeing_y, seeing_y2))
        median_see_xf=np.median(seeing_x)
        median_see_yf=np.median(seeing_y)
        plt.title('Atmospheric Seeing '+str(wdr)+'  Median Seeing Long.: '+str("%.4f"%median_see_xf)  + '"  Median Seeing Trav.: '+str("%.4f"%median_see_yf+'"'),size=10,weight="heavy",loc="center",color="Blue")
        plt.title("©IAO RoboDIMM", size=10,weight="heavy" ,loc='right',color="black")
        plt.xlabel("Time [UTC]",color="magenta",weight="heavy")
        plt.ylabel("Seeing [Arcseconds]",color="magenta",weight="heavy")
        timeArray = [datetime.strptime(i, '%Y-%m-%d %H:%M:%S.%f') for i in dte]
        timeArray2 = [datetime.strptime(i, '%Y-%m-%d %H:%M:%S.%f') for i in dte2]


        plt.plot([], [])
        plt.scatter(timeArray, seeing_x, color="blue", edgecolors="white", marker='P', linewidths=0.1, alpha=0.7,
                    label='Longitudenal', s=70)
        plt.scatter(timeArray, seeing_y, color="red", edgecolors="white", marker='X', linewidths=0.1, alpha=0.7,
                    label='Traversal', s=70)
        #plt.scatter(timeArray, seeing_x, color="orange", edgecolors="white", marker='^', linewidths=0.1, alpha=0.7,
        #            labe'Longitudenal', s=30)
        #plt.scatter(timeArray, seeing_y, color="red", edgecolors="white", marker='o', linewidths=0.1, alpha=0.7,
        #            label='Traversal', s=30)
        #plt.scatter(timeArray2, seeing_x2,color="green", edgecolors="white", marker='X', linewidths=0.1, alpha=0.7,
        #            label='Longitudenal (Fried et.al)', s=30)
        #plt.scatter(timeArray2, seeing_y2, color="blue", edgecolors="white", marker='P', linewidths=0.1, alpha=0.7,
        #            label='Traversal (Fried et.al)', s=30)
        plt.legend()
        plt.gcf().autofmt_xdate()
        myFmt = mdates.DateFormatter('%d-%m-%Y %H:%M')
        plt.gca().xaxis.set_major_formatter(myFmt)
        #plt.gcf().set_dpi(300)
        plt.savefig(str(wdr) + "/" + str(wdr) + "_seeingplot.png")
        #plt.show()
        plt.close()
        print("Seeing plot generated")
        Messenger().txtmessage(str("Seeing for: " + wdr))
        Messenger().filemessage(str(filename))
        Messenger().filemessage(str(filename2))
        Messenger().filemessage(str(wdr) + "/" + str(wdr) + "_seeingplot.png")
        os.chdir(wdr)
        os.system("rm *.fits")
        os.system("mv *Centroids.dat centroids")
        os.chdir('../')
        os.chdir(wdr+"/fitscube")
        list_of_files=glob.glob('*.fits')
        if (len(list_of_files) >= 1):
            latest_file = max(list_of_files, key=os.path.getmtime)
            Messenger().txtmessage(str("One cube file: "))
            print("Slack Uploading: ", latest_file)
            Messenger().filemessage(str(latest_file))
        os.chdir('../../')

    else:
        plt.figure(figsize=(14, 8), num='Seeing Plot')
        plt.title('Atmospheric Seeing ' + str(wdr), size=10, weight="heavy",loc="center", color="Blue")
        plt.title("©IAO RoboDIMM", size=10, weight="heavy", loc='right', color="black")
        plt.text(0.6, 0.5, "No DIMM data for: "+str(wdr), ha="right", weight="heavy",color="red")
        plt.savefig(str(wdr) + "/" + str(wdr) + "_seeingplot.png")
        #plt.show()
        os.chdir(wdr + "/fitscube")
        list_of_files = glob.glob('*.fits')
        if(len(list_of_files)>=1):
            latest_file = max(list_of_files, key=os.path.getmtime)
            Messenger().txtmessage(str("No Seeing Plot for: " + wdr))
            Messenger().filemessage(str(wdr) + "/" + str(wdr) + "_seeingplot.png")
        os.chdir('../../')

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
    print("Generating plot for: ",args.d)
    main(args.d)
