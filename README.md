<p align="center">
    <img width="200" src="https://user-images.githubusercontent.com/58334054/220020199-4ae158cd-f7ad-4377-8ea9-7cbd01e92eec.png" alt="Material Bread logo">
</p>

<h3 align="center">Robotic DIMM</h3>

---

<p align="center"> 🤖 A Differential Image Motion Monitor(DIMM) for atmospheric seeing observation.
    <br> 
</p>

## 📝 Table of Contents
+ [About](#about)
+ [Prerequisites](#getting_started)
+ [Usage](#usage)
+ [Author](#author)
+ [References](#acknowledgement)

## 🛠 About <a name = "about"></a>
The turbulent atmospheric layers cause beam propagation disturbances that degrade the quality of astronomical images
The DIMM principle involves using the same telescope to produce twin images of a star via two entrance pupils separated by a distance. The differential method measures the angular differences over the two small pupils. 
By using a turbulence model to determine the phase structure function, we can evaluate the longitudinal and transverse variances (parallel and perpendicular to the aperture alignment) of differential image motion

## ⛏️ Prerequisites <a name = "getting_started"></a>

### 
> python 3

Dependencies can be installed with:
> pip3

CMOS camera API/SDK:
> https://thinklucid.com/arena-software-development-kit/

## 💭 Usage <a name = "usage"></a>

The entire software is written in Python 3.6 <br>
If you are interested in validating data, download image cube provided in /fitscube folder and run:
```
offline_seeing_analysis.py ---- Exploit the centroid algorithm, compute seeing and save log in DIMManalysis folder
```

The codes in <a href=" https://github.com/tsewangstanzin/RoboticDIMM/tree/main/obs"> /obs </a> is responsible for conducting observation through this system configuration (Other telescope and camera would need their API/SDK):
<p align="center">
    <img width="400" src="https://user-images.githubusercontent.com/58334054/220026194-015d937c-adbf-4e22-80ca-a52bc4fe3f06.png" alt="Material Bread logo">
</p>

```
dimm.py ---- Only script that runs all the time. Responsible for overall observation conduct. Imports other scripts given below:

power_control.py ---- Control power through an Arduino based power controller
best_stars.py ---- Select appropriate star from starcatalog.lst
meade_tel_control.py ---- Control Meade telescope
webcam_pointing_v3.py ---- Compensate poor pointing by a webcam+100mm lens piggybacked
grabcube.py ---- Grab cube image at fast rate from Lucid Vison CMOS Camera. 
seeing_analysis.py ---- Exploit Fried parameters and Tokovin et al. DIMM model/paramaters and compute seeing
read_AWS.py ---- Read live weather 
auto_plotter_transfer.py ---- Plot night seeing
slack_bot.py ----  Upload plot and post observation and observing condition update on Slack

```

## ✍️  Author <a name = "author"></a>

## Connect with me
<p align="center">
	<a href="mailto:tstanzin.in@gmail.com"><img img src="https://img.shields.io/badge/gmail-%23EA4335.svg?style=plastic&logo=gmail&logoColor=white" alt="Gmail"/></a>
	<a href="https://github.com/tsewangstanzin"><img src="https://img.shields.io/badge/github-%23181717.svg?style=plastic&logo=github&logoColor=white" alt="GitHub"/></a>
	<a href="https://www.linkedin.com/in/tsewangstanzin/"><img src="https://img.shields.io/badge/linkedin-%230A66C2.svg?style=plastic&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
	<a href="https://www.facebook.com/tstanzin"><img src="https://img.shields.io/badge/facebook-%231877F2.svg?style=plastic&logo=facebook&logoColor=white" alt="Facebook"/></a>

</p>

## 🎉 References <a name = "acknowledgement"></a>
+ https://www.meade.com/downloadEntityFile/assets/product_files/instructions/LX200GPS_manual.pdf
+ http://www.company7.com/library/meade/LX200CommandSet.pdf
+ Fried D.L., 1966, PASP, 56, 1372
+ Roddier F., 1981, Prog. Optics, 19, 281
+ Sarazin M., 2001 -http://www.eso.org/astclim/espas/iran/zanjan/zanjan02.ppt
+ Sarazin M., Tokovinin A., 2002, ESO Con. andWork. proc., 58, 231
+ Tokovinin A., 2002, PASP, 114, 1156
+ Tokovinin A., Kornilov V., Shatsky N.,Voziakova O., 2003b, MNRAS, 343, 891
