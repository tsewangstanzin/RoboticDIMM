import numpy as np
import matplotlib.pyplot as plt

# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(['GDP Per Capdsfdfita (US $)'],loc='upper center')


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(['GDP Per Capita (US $)'],loc='upper right')
fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.show()
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

speed = np.array([3, 1, 2, 0, 5])
acceleration = np.array([6, 5, 7, 1, 5])

ax1 = plt.subplot()
l1, = ax1.plot(data1, color='red')
ax2 = ax1.twinx()
l2, = ax2.plot(data2, color='orange')

plt.legend([l1, l2], ["speed", "acceleration"])

plt.show()

import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import EarthLocation, SkyCoord
from pytz import timezone
from astropy.time import Time

from astroplan import Observer
from astroplan import FixedTarget
from astroplan.plots import plot_airmass,plot_sky


longitude = '78d57m53s'
latitude = '32d46m44s'
elevation = 4500 * u.m
location = EarthLocation.from_geodetic(longitude, latitude, elevation)
observer = Observer(location = location, timezone = 'Asia/Kolkata',
                             name = "IAO Hanle", description = "Meade DIMM telescope")






coordinates = SkyCoord('06h45m08.9173s', '-16d42m58.017s', frame='icrs')
target = FixedTarget(name='Sirius', coord=coordinates)

observe_time = Time('2020-06-15 23:30:00')

plot_airmass(target, observer, observe_time,style_kwargs={'linestyle': '--', 'color': 'r'},brightness_shading=True, altitude_yaxis=True)
plt.tight_layout()
plt.savefig("Airmass.png")
plt.show()

start_time = Time('2000-06-15 20:00:00')
end_time = Time('2000-06-16 04:00:00')
delta_t = end_time - start_time
now = Time.now()
sunset_iao = observer.sun_set_time(now, which='nearest')
eve_twil_iao = observer.twilight_evening_astronomical(now, which='nearest')
midnight_iao = observer.midnight(now, which='next')
morn_twil_iao = observer.twilight_morning_astronomical(now, which='next')
sunrise_iao = observer.sun_rise_time(now, which='next')
t_start = morn_twil_iao
print(type(t_start))
t_end = eve_twil_iao
observe_time = t_start + (t_end - t_start) * np.linspace(0.0, 1.0, 20)
observe_time2 = start_time + delta_t*np.linspace(0, 1, 75)

#plot_airmass(target, observer, observe_time)
target_names = ['HR 7001']
targets = [FixedTarget.from_name(target) for target in target_names]
target_names2 = ['HR 424 ']
targets2 = [FixedTarget.from_name(target) for target in target_names2]

for target in targets:
    plot_sky(target, observer, observe_time,style_kwargs={'marker': '*'})
for target in targets2:
    plot_sky(target, observer, observe_time)
plt.legend(loc=[1.1,0])
plt.xlabel("Observed Plot",color="green")
plt.savefig("OBplot.png")
plt.show()
