import re
import ephem
import numpy as np


# set up ephem Observer for the IAO site
def iao_site():
    iao = ephem.Observer()
    iao.lat = "+32:46:47"
    iao.long = "+78:57:45"
    iao.elevation = 4547
    # iao.temp = -10
    #iao.compute_pressure()
    return iao

def night_start():
    iao = iao_site()
    iao.date = ephem.now()
    sun = ephem.Sun()
    sun.compute(iao)
    current_sun_alt=float(sun.alt) * 180.0 / np.pi
    current_sun_az=float(sun.az) * 180.0 / np.pi
    # iao.horizon = '-12'
    #rise = ephem.localtime(iao.next_rising(sun))
    #set = ephem.localtime(iao.next_setting(sun))
    #now = ephem.localtime(ephem.now())
    '''
    print("prev rising: ", iao.previous_rising(ephem.Sun()))
    print("prev setting: ", iao.previous_setting(ephem.Sun()))
    print("next rise: ", iao.next_rising(ephem.Sun()))
    print("next set: ", iao.next_setting(ephem.Sun()))
    '''
    #iao.date = ephem.now()
    #print(iao.date)
    #print("LST: %s" % iao.sidereal_time())
    #t2rise = rise - now
    #t2set = set - now
    #return False
    if(current_sun_alt>-12.0):
        print("Its day time! Telescope Parked !Powered off! Having a good sleep :) ! Sun at:  %f %f "%(current_sun_az,current_sun_alt))
        return False
    elif(current_sun_alt<=-12.0):
        print("Its night time! ")
        return True
# read in HR catalog list used by turbina
def hr_catalog(site):
    fpp = open("scheduler_star.lst", "r")
    lines = fpp.readlines()
    fpp.close()
    stars = {}
    p = re.compile('#')
    for line in lines:
        if not p.match(line):
            hr=line[1:5]
            stars[hr]=ephem.readdb('HR ' + line[1:5] + ',f,' + line[6:17] + ',' + line[18:30] + ',' + line[53:57] + ',2000')
            if site:
                stars[hr].compute(site)
    return stars
    '''
    fp = open("scheduler_star.lst", "r")
    lines = fp.readlines()
    fp.close()
    stars = {}

    p = re.compile('#')
    for line in lines:

        if not p.match(line):
            hr = line[0:4].strip()
            name = line[5:12]
            h = line[13:15]
            m = line[16:18]
            s = line[19:21]
            ra = "%s:%s:%s" % (h, m, s)

            sign = line[22:23]
            d = line[24:26]
            m = line[27:29]
            s = line[30:32]
            dec = "%s%s:%s:%s" % (sign, d, m, s)

            vmag = float(line[33:38])
            bmv = float(line[39:44])
            sed = line[45:48]
            sptype = line[49:63]
            dbstr = "%s,f|S|%s,%s,%s,%f,2000" % (name, sptype, ra, dec, vmag)
            # print(dbstr)
            stars[hr] = ephem.readdb(dbstr)
            if site:
                stars[hr].compute(site)
    return stars
    '''
