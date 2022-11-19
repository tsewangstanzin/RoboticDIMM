'''
from skyfield.api import Star, load
from skyfield.data import hipparcos

with load.open(hipparcos.URL) as f:
    df = hipparcos.load_dataframe(f)

#barnards_star = Star.from_dataframe(df.loc[87937])
#print(barnards_star)
planets = load('de421.bsp')
earth = planets['earth']

ts = load.timescale()
t = ts.now()
#astrometric = earth.at(t).observe(barnards_star)
#ra, dec, distance = astrometric.radec()
#print(ra)
#print(dec)
df = df[df['magnitude'] <= 1.5]
print('After filtering, there are {} stars'.format(len(df)))
print(df)
'''
from numpy import array, zeros, ones, arange, where, argsort
import ephem
import datetime as dt
import re
import numpy as np
import time
''' Read entire Bright Star Catalog and return a list of PyEphem sources
   '''

filename = '/home/iiap/BrightStarCatalog.txt'

f = open(filename, 'r')


# Read two header lines (and ignore them)
line = f.readline()
line = f.readline()
srcs = []

# Loop over lines in file
for line in f.readlines():
    srcs.append(ephem.readdb('HR ' + line[1:5] + ',f,' + line[6:17] + ',' + line[18:30] + ',' + line[53:57] + ',2000'))
f.close()
# Do an initial compute so that name, ra, dec, etc. are accessible.  Will override with compute for
# observer later.
i=0
temp= []
count=0
for src in srcs:
    src.compute()
    if(src.mag<4.0):
        print(src.name,  src.ra,src.dec ,src.mag, 'J2000')
        count+=1

        for word in src.name.split():
            if word.isdigit():
                t2=word
        temp.append(t2)

f.close()
print(count)

fp = open("/home/iiap/BrightStarCatalog.txt", "r")
lines2 = fp.readlines()
fp.close()


visitedstar=open("newcatalog.txt", "w")
t=0
for t in range(len(temp)):
      for line2 in lines2:
        #print(ss)
        # find() returns -1 if no match is found
        if  line2[1:5].strip()==temp[t]:
            #print(line2)
            visitedstar.write(line2)
            #pass
visitedstar.close()
'''
iao = ephem.Observer()
iao.lat = "+32:46:46"
iao.long = "+78:58:28"
iao.elevation = 4308
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
        if iao:
            stars[hr].compute(iao)
        #print(stars)

        #print("Star Name= %s; Mag= %f; Airmass= %f;  HA = %s;  Alt = %s;  Az = %s" % (
            #stars.name, stars.mag, airmass, ha, star.alt, star.az))


while(1):
    iao = ephem.Observer()
    iao.lat = "+32:46:46"
    iao.long = "+78:58:28"
    iao.elevation = 4308
    iao.date = ephem.now()
    #obs.pressure = pressure / 100.  # convert to mBar
    #obs.temp = temperature
    #obs.horizon = horizon
   

    fpp = open("scheduler_star.lst", "r")
    lines = fpp.readlines()
    fpp.close()
    stars = {}
    p = re.compile('#')
    for line in lines:
        if not p.match(line):
            hr=line[1:5]
            stars[hr]=ephem.readdb('HR ' + line[1:5] + ',f,' + line[6:17] + ',' + line[18:30] + ',' + line[53:57] + ',2000')
            if iao:
                stars[hr].compute(iao)


    good = []
    el_limit = 30.0 * ephem.pi / 180.0
    az_limit = 0.0 * ephem.pi / 180.0
    for key, star in stars.items():
        dec=float(star.dec)* 180.0 / np.pi
        if star.az > az_limit and star.alt > el_limit and dec>0.0 and dec <50.0:
            good.append(key)
    sorted_good= []
    for x in good:
        a=float(stars[x].alt)
        sorted_good.append([x,a])
    sorted_good.sort(key = lambda x: x[1],reverse=True)
    good=[]
    for x in sorted_good:
        good.append(x[0])
    #print(good)

    print("\nPointing")
    for s in good:
        iao.date = ephem.now()

        star = stars[s]
        #a_ra, a_dec — Astrometric Geocentric Position for the star atlas epoch you’ve specified
        #g_ra, g_dec — Apparent Geocentric Position for the epoch-of-date
        #ra, dec — Apparent Topocentric Position for the epoch-of-date
        star.compute(iao)
        lst = iao.sidereal_time()
        ha = ephem.hours(lst - star.ra)
        if star.alt > 0.0:
            airmass = 1 / np.cos(ephem.degrees('90:00:00') - star.alt)
        else:
            airmass = 999.0
        print("Name= %s; C_RA= %s; C_DEC= %s; A_RA= %s; A_DEC= %s; Mag= %f; AMass= %f;  HA = %s;  LST= %s; Alt = %s;  Az = %s" % (
           star.name,star.a_ra,star.a_dec, star.ra,star.dec,star.mag, airmass, ha,lst, star.alt, star.az))
    time.sleep(3)
'''