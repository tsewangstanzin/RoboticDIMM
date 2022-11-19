from meade_tel_control import Telescope
import time
def main():
    print("1. Update Meade time and location (From GPS)")
    print("2.Get telescope current date, time and location ")
    print("3. Set speed to slew rate and do pointing (Human intervention needed later for offset [poor meade pointing])")
    print("4. Set to guide rate and do auto guiding")
    t1=Telescope(3, '/dev/ttyUSB0')
    #MeadeGPSUpdate=t1.setGPS()
    #print(MeadeGPSUpdate)
    #time.sleep(60)
    #print("GPS updated succesfully")
    '''
    alt=t1.getTelAlt()
    print(alt)
    print(alt.decode('latin-1'))
    alt=alt.decode('latin-1')
    import re
    alt_dms=re.split('[ß : #]', alt)

    if(float(alt_dms[0])<0):
        alt_decimal = float(alt_dms[0]) - float(alt_dms[1]) / 60 - float(alt_dms[2]) / (60 * 60)
        print(alt_decimal)
    else:
        alt_decimal=float(alt_dms[0]) + float(alt_dms[1]) / 60 + float(alt_dms[2]) / (60 * 60)
        print(alt_decimal)
    h = t1.HomeStatus()
    s = h.decode('UTF-8')
    
    #s=int(float(s))
    if(s==1):
        print("Homed already")
    
    #Toggle to set precision to high
    telRA=t1.getTelRA()
    if(len(telRA)==8):
        t1.setPrecision()
        print("Changed to High precision mode")
    else:
        print("In high precision mode")
    '''
    #eluplimit=t1.setUpperLimit()
    #ellowlimit=t1.setLoweLimit()
    #print(ellowlimit,eluplimit)
    #Confirm what we have set
    #time.sleep(10)

    Meadetime=t1.gettelescopeTime()
    print(Meadetime)
    #time.sleep(10)
    t1.setSpeed(3)
    slew_flag=t1.RADECPointing('11','35','2','+','37','48','3')
    if(slew_flag.decode('latin-1')=='0'):
        print("Slew command accepted")
    else:
        print("Out of Limit")
    sr = t1.getSlewStatus()
    distance_bars=len(sr)
    while (distance_bars != 1):
        sr = t1.getSlewStatus()
        distance_bars = len(sr)
        print("Slewing...")
    print("Slew Complete")
    print("Tel Coordinates:")
    shms=t1.getTelRA()
    sdms=t1.getTelDEC()
    print(shms)
    print(sdms)
    #time.sleep(30)
    #sr=t1.getSlewStatus()
    #s=sr.decode('latin-1')
    #while(s!='#'):
    #    s = sr.decode('latin-1')
    #    print("Slewing...")

    #print(sr.decode('latin-1'))
    #time.sleep(60)
    #sr = t1.getSlewStatus()
    #print(sr.decode('latin-1'))


    '''
    slew_flag=slew_flag.decode('UTF-8')

    print(type(slew_flag))
    slew_flag = int(slew_flag)
    print(type(slew_flag))
    if (slew_flag == 0):
        print("Slew Possible")
    elif (slew_flag == 1):
        print("Below Horizon")
    elif (slew_flag == 2):
        print("Too high ")
    #time.sleep(30)
    #t1.Park()
    '''


    

if __name__ == '__main__':
    main()