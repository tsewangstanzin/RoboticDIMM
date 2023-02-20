<p align="center">
    <img width="200" src="https://user-images.githubusercontent.com/58334054/220020199-4ae158cd-f7ad-4377-8ea9-7cbd01e92eec.png" alt="Material Bread logo">
</p>

<h3 align="center">Robotic DIMM</h3>

---

<p align="center"> 🤖 A Differential Image Motion Monitor(DIMM) for atmospheric seeing observation is developed at the Indian Astronomical Observatory, Hanle, India.
    <br> 
</p>

## 📝 Table of Contents
+ [About](#about)
+ [Usage](#usage)
+ [Getting Started](#getting_started)
+ [Deploying your own bot](#deployment)
+ [Built Using](#built_using)
+ [TODO](../TODO.md)
+ [Contributing](../CONTRIBUTING.md)
+ [Authors](#authors)
+ [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>
The turbulent atmospheric layers cause beam propagation disturbances that degrade the quality of astronomical images
The DIMM principle involves using the same telescope to produce twin images of a star via two entrance pupils separated by a distance. The differential method measures the angular differences over the two small pupils. 
By using a turbulence model to determine the phase structure function, we can evaluate the longitudinal and transverse variances (parallel and perpendicular to the aperture alignment) of differential image motion

## 💭 Usage <a name = "usage"></a>
The entire software is written in Python 3.6 <br>
The code in <a href=" https://github.com/tsewangstanzin/RoboticDIMM/tree/main/obs"> /obs </a> is responsible for conducting observation through this system configuration (Other telescope and camera would need their API/SDK):
<p align="center">
    <img width="400" src="https://user-images.githubusercontent.com/58334054/220026194-015d937c-adbf-4e22-80ca-a52bc4fe3f06.png" alt="Material Bread logo">
</p>


```
dimm.py ---- Only script that runs all the time. Responsible for overall observation conduct. Imports other scripts given below:

power_control.py ---- Control power through an Arduino based power controller
best_stars.py ---- Select appropriate star from starcatalog.lst
meade_tel_control.py ---- Control Meade telescope
webcam_pointing_v3.py ---- Compensate poor pointing by a webcam+100mm lens piggybacked
grabcube.py ---- Grab cube image at fast rate from Lucid Vison Camera. SDK: https://thinklucid.com/arena-software-development-kit/
seeing_analysis.py ---- Exploit Fried parameters and Tokovin et al. DIMM model/paramaters and compute seeing
read_AWS.py ---- Read live weather 
auto_plotter_transfer.py ---- Plot night seeing
slack_bot.py ----  Upload plot and post observation and observing condition update on Slack

```
The first part, i.e. "!dict" **is not** case sensitive.

The bot will then give you the Oxford Dictionary (or Urban Dictionary; if the word does not exist in the Oxford Dictionary) definition of the word as a comment reply.

### Example:

> !dict what is love

**Definition:**

Baby, dont hurt me~
Dont hurt me~ no more.

**Example:**

Dude1: Bruh, what is love?
Dude2: Baby, dont hurt me, dont hurt me- no more!
Dude1: dafuq?

**Source:** https://www.urbandictionary.com/define.php?term=what%20is%20love

---

<sup>Beep boop. I am a bot. If there are any issues, contact my [Master](https://www.reddit.com/message/compose/?to=PositivePlayer1&subject=/u/Wordbook_Bot)</sup>

<sup>Want to make a similar reddit bot? Check out: [GitHub](https://github.com/kylelobo/Reddit-Bot)</sup>

## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## 🚀 Deploying your own bot <a name = "deployment"></a>
![Working](https://media.giphy.com/media/20NLMBm0BkUOwNljwv/giphy.gif)
To see an example project on how to deploy your bot, please see my own configuration:

+ **Heroku**: https://github.com/kylelobo/Reddit-Bot#deploying_the_bot

## ⛏️ Built Using <a name = "built_using"></a>
+ [PRAW](https://praw.readthedocs.io/en/latest/) - Python Reddit API Wrapper
+ [Heroku](https://www.heroku.com/) - SaaS hosting platform

## ✍️ Authors <a name = "authors"></a>
+ [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
+ Hat tip to anyone whose code was used
+ Inspiration
+ References

## Hey 👋, I'm [Pavan Gandhi!](https://github.com/iampavangandhi/)

[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=Linkedin&logoColor=white)](https://linkedin.com/in/iampavangandhi)
[![Website Badge](https://img.shields.io/badge/Website-3b5998?style=flat-square&logo=google-chrome&logoColor=white)](https://iampavangandhi.github.io/)
[![Twitter Badge](https://img.shields.io/badge/-Twitter-00acee?style=flat-square&logo=Twitter&logoColor=white)](https://twitter.com/iampavangandhi)
[![Instagram Badge](https://img.shields.io/badge/-Instagram-e4405f?style=flat-square&logo=Instagram&logoColor=white)](https://instagram.com/iampavangandhi/)
[![Telegram Badge](https://img.shields.io/badge/-Telegram-0088cc?style=flat-square&logo=Telegram&logoColor=white)](https://t.me/iampavangandhi)

### Glad to see you here! &nbsp; ![](https://visitor-badge.glitch.me/badge?page_id=iampavangandhi.iampavangandhi&style=flat-square&color=0088cc)

I'm a graduate in Computer Science 🎓 from Delhi University 🏛. I'm a passionate learner who's always willing to learn and work across technologies and domains 💡. I love to explore new technologies and leverage them to solve real-life problems ✨. Apart from that I also love to guide and mentor newbies 👨🏻‍💻. I'm currently into Web Development 🕸️ and working on my Data Structures and Algorithms 🤓.

Joined Github **{{ ACCOUNT_AGE }}** years ago.

Since then I pushed **{{ COMMITS }}**+ commits, opened **{{ ISSUES }}**+ issues, submitted **{{ PULL_REQUESTS }}**+ pull requests, created **{{ GISTS }}**+ gists and contributed to **{{ REPOSITORIES_CONTRIBUTED_TO }}**+ public repositories.

Like My Work?

<a href="https://www.buymeacoffee.com/iampavangandhi" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="60px" width="217px" ></a>

[![](https://gitwar.herokuapp.com/badge?username=iampavangandhi&label=Gitwar%20Profile%20Score&style=for-the-badge&color=0088cc)](https://gitwar.herokuapp.com/)

<img align="right" height="250" width="375" alt="" src="https://raw.githubusercontent.com/iampavangandhi/iampavangandhi/master/gifs/coder.gif" />

### Talking about Personal Stuffs:

- 🛠 &nbsp; I’m currently working with Nodejs, Express, React, <br /> Graphql, Mongodb, Javascript, etc.
- 🚀 &nbsp; I’m currently learning Full Stack Development.
- 👨🏻‍💻 &nbsp; Most of my projects are available on [Github](https://github.com/iampavangandhi).
- 💬 &nbsp; Ask me about anything [here](https://github.com/iampavangandhi/iampavangandhi/issues/2)! I am happy to help.
- 👾 &nbsp; Fun fact: Equal is Not Always Equal in Javascript.
- 📫 &nbsp; How to reach me: pavangandhi100@gmail.com.
- 📝 &nbsp; Checkout my [Resume](https://github.com/iampavangandhi/iampavangandhi/blob/master/resume.pdf).

### My Absolute Favorites:

- 💻 &nbsp; I love exploring new tech stack and building cool stuffs.
- 📰 &nbsp; Reading & writing tech blogs whenever possible.
- 🍕 &nbsp; Hackathons, meetups & tech events.

### Languages and Tools:

<code><img height="27" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/cpp/cpp.png" alt="cpp"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" alt="python"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png" alt="javascript"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/nodejs/nodejs.png" alt="nodejs"></code>
<code><img height="27" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/express/express-original.svg" alt="expressjs"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/react/react.png" alt="react"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/graphql/graphql.png" alt="graphql"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/sql/sql.png" alt="sql"></code>
<code><img height="27" src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSTTzPAw-55ssm1Im594xYZ9eRQu2JylrkYLg&usqp=CAU" alt="mongodb"></code>
<code><img height="27" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" alt="git"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/terminal/terminal.png" alt="terminal"></code>

<!--
<code><img height="25" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/sass/sass.png" alt="sass"></code>
-->

### Projects and Dev Stuffs:

<details>	
  <summary><b>⚡ Github Stats</b></summary>

  <br />
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=iampavangandhi&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=iampavangandhi&exclude_repo=KNN-Image-Classification&show_icons=true&hide_border=true&layout=compact&langs_count=8"/>
</details>

<details>	
  <summary><b>☄️ Github Streaks</b></summary>

  <br />
  <img height="180em" src="https://github-readme-streak-stats.herokuapp.com/?user=iampavangandhi&hide_border=true" />
</details>

<details>
  <summary><b>🧑‍🚀 Open Source Projects</b></summary>

  <br />
  <table>
    <thead align="center">
      <tr border: none;>
        <td><b>💻 Projects</b></td>
        <td><b>🌟 Stars</b></td>
        <td><b>🍴 Forks</b></td>
        <td><b>🐛 Issues</b></td>
        <td><b>🔔 Pull Requests</b></td>
        <td><b>👨‍💻 Language</b></td>
      </tr>
    </thead>
    <tbody>
      <tr>
	      <td><a href="https://github.com/iampavangandhi/Gitwar"><b>🚀 Gitwar</b></a></td>
        <td><img alt="Stars" src="https://img.shields.io/github/stars/iampavangandhi/Gitwar?style=flat-square&labelColor=343b41"/></td>
        <td><img alt="Forks" src="https://img.shields.io/github/forks/iampavangandhi/Gitwar?style=flat-square&labelColor=343b41"/></td>
        <td><img alt="Issues" src="https://img.shields.io/github/issues/iampavangandhi/Gitwar?style=flat-square"/></td>
        <td><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/iampavangandhi/Gitwar?style=flat-square"/></td>
        <td><img alt="Language" src="https://img.shields.io/github/languages/top/iampavangandhi/Gitwar?style=flat-square"/></td>
      </tr>
      <tr>
	      <td><a href="https://github.com/iampavangandhi/TradeByte"><b>💸 TradeByte</b></a></td>
        <td><img alt="Stars" src="https://img.shields.io/github/stars/iampavangandhi/TradeByte?style=flat-square&labelColor=343b41"/></td>
        <td><img alt="Forks" src="https://img.shields.io/github/forks/iampavangandhi/TradeByte?style=flat-square&labelColor=343b41"/></td>
        <td><img alt="Issues" src="https://img.shields.io/github/issues/iampavangandhi/TradeByte?style=flat-square"/></td>
        <td><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/iampavangandhi/TradeByte?style=flat-square"/></td>
        <td><img alt="Language" src="https://img.shields.io/github/languages/top/iampavangandhi/TradeByte?label=javascript&style=flat-square"/></td>
      </tr>
      <tr>
	      <td><a href="https://github.com/iampavangandhi/TheNodeCourse"><b>👨🏻‍💻 TheNodeCourse</b></a></td>
        <td><img alt="Stars" src="https://img.shields.io/github/stars/iampavangandhi/TheNodeCourse?style=flat-square&labelColor=343b41"/></td>
        <td><img alt="Forks" src="https://img.shields.io/github/forks/iampavangandhi/TheNodeCourse?style=flat-square&labelColor=343b41"/></td>
        <td><img alt="Issues" src="https://img.shields.io/github/issues/iampavangandhi/TheNodeCourse?style=flat-square"/></td>
        <td><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/iampavangandhi/TheNodeCourse?style=flat-square"/></td>
        <td><img alt="Language" src="https://img.shields.io/github/languages/top/iampavangandhi/TheNodeCourse?style=flat-square"/></td> 
      </tr>
      <tr>
	      <td><a href="https://github.com/iampavangandhi/iampavangandhi"><b>🤓 iampavangandhi</b></a></td>
        <td><img alt="Stars" src="https://img.shields.io/github/stars/iampavangandhi/iampavangandhi?style=flat-square&labelColor=343b41"/></td>
        <td><img alt="Forks" src="https://img.shields.io/github/forks/iampavangandhi/iampavangandhi?style=flat-square&labelColor=343b41"/></td>
        <td><img alt="Issues" src="https://img.shields.io/github/issues/iampavangandhi/iampavangandhi?style=flat-square"/></td>
        <td><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/iampavangandhi/iampavangandhi?style=flat-square"/></td>
        <td><img alt="Language" src="https://img.shields.io/badge/markdown-100%25-blue?style=flat-square"/></td> 
      </tr>
    </tbody>
  </table>
  <br />
</details>
 
<details>	
  <br />
  <summary><b>⚙️ Things I use to get stuff done</b></summary>
  	<ul>
  	    <li><b>OS:</b> Ubuntu 20.04</li>
	    <li><b>Laptop: </b> HP Elitebook (i5)</li>
  	    <li><b>Browser: </b> Firefox Web Browser</li>
	    <li><b>Terminal: </b> ZSH: Oh My Zsh (PowerLevel10k)</li>
	    <li><b>Code Editor:</b> VSCode - The best editor out there.</li>
	    <li><b>To Stay Updated:</b> Dev.to, Medium, Linkedin and Twitter.</li>
	    <br />
	⚛️ Checkout My VSCode Configrations <a href="https://gist.github.com/iampavangandhi/039b1dc5a7cdcb007ab3691814d53130">Here</a>.
	</ul>	
</details>

#

<div align="center">

### Show some ❤️ by starring some of the repositories!

</div>



<h1 align="center">Hi 👋, I'm <a href="https://100rabhcsmc.github.io/Me.io/" target="blank">
Saurabh</a></h1>
<h3 align="center">A passionate Mobile App developer from Pune India &#127470;&#127475</h3>

<p align="left"> <img src="https://komarev.com/ghpvc/?username=100rabhcsmc&label=Profile%20views&color=0e75b6&style=flat" alt="100rabhcsmc" /> </p>

<p align="left"> <a href="https://twitter.com/100rabhcsmc" target="blank"><img src="https://img.shields.io/twitter/follow/100rabhcsmc?logo=twitter&style=for-the-badge" alt="100rabhcsmc" /></a> </p>

<a target="_blank" align="center">
  <img align="right" top="500" height="300" width="400" alt="GIF" src="https://media.giphy.com/media/SWoSkN6DxTszqIKEqv/giphy.gif">
</a>

- 🔭 I’m currently working in <a href="https://phoenix.tech/griffyn/" target="blank">Griffyn Robotech Private Limited</a>

- 🌱 I’m currently Working on Mobile App(React-Native)

- 🤝 I’m available for freelancing.

- 🌱 I’m currently learning Swift && SwiftUI <a href="https://github.com/100rabhcsmc/100DaysOfSwift" target="blank">100DaysOfSwift</a>

- 📝 I regularly write articles on [https://dev.to/100rabhcsmc](https://dev.to/100rabhcsmc)

- 💬 Ask me about **Reactjs & React-Native**

- 📫 How to reach me **saurabhchavan052@gmail.com**

- 📄 Know about my experiences <a href="https://github.com/100rabhcsmc/Me.io/blob/master/01SaurabhChavanReactNativeResume.pdf" target="blank">Resume</a>
<br/>
<h3 align="center" > <img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="30" height="30" style="margin-right: 10px;">Connect with me 🤝 </h3>

<p align="center">

 <div align="center"  class="icons-social" style="margin-left: 10px;">
        <a style="margin-left: 10px;"  target="_blank" href="https://www.linkedin.com/in/saurabhmchavan/">
			<img src="https://img.icons8.com/doodle/40/000000/linkedin--v2.png"></a>
        <a style="margin-left: 10px;" target="_blank" href="https://github.com/100rabhcsmc">
		<img src="https://img.icons8.com/doodle/40/000000/github--v1.png"></a>
		<a style="margin-left: 10px;" target="_blank" href="https://stackoverflow.com/users/12053852/saurabh-chavan?tab=profile">
				<img src="https://img.icons8.com/external-tal-revivo-color-tal-revivo/40/000000/external-stack-overflow-is-a-question-and-answer-site-for-professional-logo-color-tal-revivo.png"></a>
	   <a style="margin-left: 10px;" target="_blank" href="https://dev.to/100rabhcsmc">
					<img src="https://img.icons8.com/external-sketchy-juicy-fish/0.6x/external-blog-online-services-sketchy-sketchy-juicy-fish.png"></a>
        <a style="margin-left: 10px;" target="_blank" href="https://instagram.com/100rabhch">
			<img src="https://img.icons8.com/doodle/40/000000/instagram-new--v2.png"></a>
		<a style="margin-left: 10px;" target="_blank" href="https://twitter.com/100rabhcsmc">
			<img src="https://img.icons8.com/doodle/1x/twitter-squared--v2.png" ></a>
		<a style="margin-left: 10px;" target="_blank" href="https://www.youtube.com/channel/UC-ZdNkKNHC6KguDqNFKO2Nw?view_as=subscriber">
				<img src="https://img.icons8.com/doodle/1x/youtube--v2.png" ></a>
		<a style="margin-left: 5px;" target="_blank" href="https://github.com/100rabhcsmc/Me.io/blob/master/01SaurabhChavanReactNativeResume.pdf">
					<img src="https://img.icons8.com/plasticine/0.5x/resume.png" ></a>
      </div>

</p>

### Blogs posts

<!-- BLOG-POST-LIST:START -->

- [Download Instagram profile picture using python](https://dev.to/100rabhcsmc/instagram-profile-picture-download-using-python-n2j)
- [Convert a image to sketch using python](https://dev.to/100rabhcsmc/convert-a-image-to-sketch-using-python-3ip1)
- [Upload your project/files in GitHub using commands](https://dev.to/100rabhcsmc/upload-your-project-files-in-github-using-commands-1hn8)
<!-- BLOG-POST-LIST:END -->

---

Credit: [Saurabh Chavan](https://github.com/100rabhcsmc)

Last Edited on: 08/08/2022

<h1 align="center">Hi , I'm Ahmed Hossam <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="35"></h1>
<p align="center">
  <a href="https://github.com/DenverCoder1/readme-typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=Time+New+Roman&color=%23C8BE25&size=25&center=true&vCenter=true&width=600&height=100&lines=Software+Engineer+@bld.ai;Computer+Science+Student;Competitive+Programmer;2x+ACPC+Finalist;Expert+on+Codeforces;Division+1+on+Codechef+(5+Stars);4+Kyu+on+Atcoder;Always+learning+new+things"></a>
</p>


<br>

<p align="center"> 
	<img src="https://komarev.com/ghpvc/?username=7oSkaaa&label=Profile%20views&color=0047AB&style=plastic?" alt="7oSkaaa" height=25px, width=160px/> 
	<!---
		<a href = "https://commits.top/egypt.html" target="_blank">
			<img src="https://aktive.tk/egypt/7oSkaaa?color=red" alt="Most Active Users" target="_blank" height=25px, width=250px/> 
		</a>
	-->
	<a href = "https://commits.top/egypt.html" target="_blank">
		<img src="https://enfsgag3ayy6w9q.m.pipedream.net/&style=plastic" alt="7oSkaaa" target="_blank" height=25px, width=250px/> 
	</a>

</p>

	
## <picture><img src = "https://github.com/7oSkaaa/7oSkaaa/blob/main/Images/about_me.gif?raw=true" width = 50px></picture> About me

<picture> <img align="right" src="https://github.com/7oSkaaa/7oSkaaa/blob/main/Images/Right_Side.gif?raw=true" width = 250px></picture>

<br><br>

- :school: I am a `Junior` at [Faculty of Computers & Informatics](http://suez.edu.eg/ar/%d9%83%d9%84%d9%8a%d8%a9-%d8%a7%d9%84%d8%ad%d8%a7%d8%b3%d8%a8%d8%a7%d8%aa-%d9%88%d8%a7%d9%84%d9%85%d8%b9%d9%84%d9%88%d9%85%d8%a7%d8%aa/) at [Suez Canal University](http://suez.edu.eg/ar/).
- :trophy: 2x `ACPC` Finalist.
- :technologist: I love using Software as a solution for every `Problem`.
- :computer: I am a competitive programmer at `Codeforces`, `Atcoder`, `Leetcode`, `Codechef`, `Google Contests`.
- :student: I’m currently learning `Computer Science` and `Software Engineering`.
- :nerd_face: Always `learning new things`.
- :thinking: I’m currently open for a new `job opportunity`, this is [MY RESUME](http://lnkiy.in/Ahmed_Hossam_Resume).
- :boom: You can visit [MY WEBSITE](https://cutt.ly/Ahmed_Hossam_Website).
<br>


## <picture> <img src="https://github.com/7oSkaaa/7oSkaaa/blob/main/Images/competitive_programming_profile.png?raw=true" width=40> </picture> My Competitive Programming Profiles

<p align="center">
  <a href="https://codeforces.com/profile/7oSkaaa"><img src="https://img.icons8.com/external-tal-revivo-shadow-tal-revivo/50/000000/external-codeforces-programming-competitions-and-contests-programming-community-logo-shadow-tal-revivo.png" alt="Code Forces"/></a>
	<a href="https://leetcode.com/7oSkaa/"><img src="https://img.icons8.com/external-tal-revivo-shadow-tal-revivo/50/000000/external-level-up-your-coding-skills-and-quickly-land-a-job-logo-shadow-tal-revivo.png" alt="LeetCode"/></a>
	<a href="https://atcoder.jp/users/ahmed_7oSkaa"><img src="https://i.ibb.co/Q9WSjDB/logo.png" alt="AtCoder" width = 60px/></a>
	<a href="https://www.codechef.com/users/ahmed_7oskaa"><img src="https://img.icons8.com/color/50/000000/codechef.png" alt="Code Chef"/></a>
	<a href="https://icpc.global/ICPCID/IW0X0CTD0ZV9"><img src="https://i.ibb.co/6J0r7rW/Daco-5610880.png" alt="ICPC Global" width = 60px /></a>     
	<a href="https://www.codingame.com/profile/e5e56c7585fda3b457056b85180a4d636850344" ><img src="https://i.ibb.co/1MRppTC/codingame-1.png" alt="Codingame" width="100" height="50">
</p>

## <picture> <img src="https://github.com/7oSkaaa/7oSkaaa/blob/main/Images/Connect-with-me.gif?raw=true" width="100px"> </picture> Connect with me
<p align="center">
	<a href="mailto:ahmed.7oskaa@gmail.com"><img img src="https://img.shields.io/badge/gmail-%23EA4335.svg?style=plastic&logo=gmail&logoColor=white" alt="Gmail"/></a>
	<a href="https://github.com/7oSkaaa"><img src="https://img.shields.io/badge/github-%23181717.svg?style=plastic&logo=github&logoColor=white" alt="GitHub"/></a>
	<a href="https://wa.me/0201208822340"><img src="https://img.shields.io/badge/whatsapp-%2325D366.svg?style=plastic&logo=whatsapp&logoColor=white" alt="Whatsapp"/></a>
	<a href="https://www.linkedin.com/in/7oskaa/"><img src="https://img.shields.io/badge/linkedin-%230A66C2.svg?style=plastic&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
	<a href="https://www.facebook.com/7oSkaaa"><img src="https://img.shields.io/badge/facebook-%231877F2.svg?style=plastic&logo=facebook&logoColor=white" alt="Facebook"/></a>
	<a href="https://www.instagram.com/ahmed_7oskaa/"><img src="https://img.shields.io/badge/instagram-%23E4405F.svg?style=plastic&logo=instagram&logoColor=white" alt="Instagram"/></a>
	<a href="https://msng.link/o/?ahmed.7oskaa=sc"><img src="https://img.shields.io/badge/snapchat-%23FFFC00.svg?style=plastic&logo=snapchat&logoColor=black" alt="Snap Chat"/></a>
</p>



## 🛠️ My Skills

### <picture> <img src = "https://github.com/7oSkaaa/7oSkaaa/blob/main/Images/Programming_Languages.gif?raw=true" width = 50px>  </picture> Programming languages

<p align="center"> 
  &emsp; 
  <a href="https://www.cprogramming.com/" target="_blank"> 
    <img alt="C" src="https://img.shields.io/badge/C%20-%232370ED.svg?style=plastic&logo=c&logoColor=white">
  </a> 
  &emsp;
  <a href="https://www.w3schools.com/cpp/" target="_blank"> 
    <img alt="C++" src="https://img.shields.io/badge/C++%20-%2300599C.svg?style=plastic&logo=c%2B%2B&logoColor=white">
  </a> 
  &emsp;
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"> 
     <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript%20-%23F7DF1E.svg?style=plastic&logo=javascript&logoColor=black">
   </a>
  &emsp;
  <a href="https://www.java.com" target="_blank"> 
    <img alt="Java" src="https://img.shields.io/badge/Java-%23007396.svg?style=plastic&logo=java&logoColor=white">
  </a>
  &emsp;
   <a href="https://www.python.org" target="_blank">
    <img alt="Python" src="https://img.shields.io/badge/Python%20-%2314354C.svg?style=plastic&logo=python&logoColor=white">
  </a>
</p>

### <picture> <img src = "https://github.com/7oSkaaa/7oSkaaa/blob/main/Images/Front_End.gif?raw=true" width = 50px>  </picture> Frontend Development
<p align="center"> 
  &emsp; 
  <a href="https://www.w3.org/html/" target="_blank"> 
   <img alt="HTML" src="https://img.shields.io/badge/HTML5%20-%23E34F26.svg?style=plastic&logo=html5&logoColor=white">
  </a>   
  &emsp;
  <a href="https://www.w3schools.com/css/" target="_blank">
    <img alt="CSS" src="https://img.shields.io/badge/CSS%20-%231572B6.svg?style=plastic&logo=css3&logoColor=white">
  </a> 
  &emsp;
  <a href="https://www.python.org" target="_blank">
    <img alt="Python" src="https://img.shields.io/badge/react-%2361DAFB.svg?style=plastic&logo=React&logoColor=black">
  </a>
  &emsp;
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"> 
     <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript%20-%23F7DF1E.svg?style=plastic&logo=javascript&logoColor=black">
   </a>
</p>

 ### <picture> <img src = "https://github.com/7oSkaaa/7oSkaaa/blob/main/Images/Software_Tools.gif?raw=true" width = 50px>  </picture> Software & Tools
 
<p align="center">
  &emsp;
    <a href="#"><img alt="Git" src="https://img.shields.io/badge/Git%20-%23F05033.svg?style=plastic&logo=git&logoColor=white"></a>
  &emsp;
    <a href="#"><img alt="GitHub" src="https://img.shields.io/badge/github-%23181717.svg?style=plastic&logo=github&logoColor=white"></a>
  &emsp;
    <a href="#"><img alt="Google Sheets" src="https://img.shields.io/badge/Google%20Sheets%20-%2334A853.svg?style=plastic&logo=google%20sheets&logoColor=white"></a>
  &emsp;
    <a href="#"><img alt="Mark Down" src="https://img.shields.io/badge/Markdown-000000?style=plastic&logo=markdown&logoColor=white"></a>
  &emsp;
    <a href="#"><img alt="Stack Overflow" src="https://img.shields.io/badge/-Stack%20Overflow-FE7A16?style=plastic&logo=stack-overflow&logoColor=white"></a>
  &emsp;
    <a href="#"><img alt="Geekf For Geeks" src="https://img.shields.io/badge/geeksforgeeks-%230F9D58.svg?style=plastic&logo=geeksforgeeks&logoColor=white"></a>
  &emsp;
    <a href="#"><img alt="JSON" img src="https://img.shields.io/badge/json-%23000000.svg?style=plastic&logo=json&logoColor=white"></a>
  &emsp;
    <a href="#"><img alt="OpenGL" src="https://img.shields.io/badge/opengl-%235586A4.svg?style=plastic&logo=opengl&logoColor=white"></a>
  &emsp;
    <a href="#"><img alt="Selenium" src="https://img.shields.io/badge/selenium-%2343B02A.svg?&style=plastic&logo=selenium&logoColor=white"></a>
    &emsp;
    <a href="#"><img src="https://img.shields.io/badge/latex-%23008080.svg?&style=plastic&logo=latex&logoColor=white" /></a>
    &emsp;
    <a href="#"><img src="https://img.shields.io/badge/django-%23092E20.svg?&style=plastic&logo=django&logoColor=white" /></a>
    &emsp;
    <a href="#"><img src="https://img.shields.io/badge/mysql-%234479A1.svg?&style=plastic&logo=mysql&logoColor=white"/></a>
</p>

 ### <picture> <img src = "https://github.com/7oSkaaa/7oSkaaa/blob/main/Images/IDEs.gif?raw=true" width = 50px>  </picture> IDEs
 
<p align="center">
  &emsp;
    <a href="#"><img alt="Visual Studio Code" src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=plastic&logo=visual-studio-code&logoColor=white"></a>
  &emsp;
    <a href="#"><img alt="JetBrain" src="https://img.shields.io/badge/jetbrains-%23000000.svg?style=plastic&logo=jetbrains&logoColor=white" /></a>
  &emsp;
    <a href="#"><img alt="Atom" src="https://img.shields.io/badge/atom-%2366595C.svg?&style=plastic&logo=atom&logoColor=white" /></a>
  &emsp;
    <a href="#"><img alt="Eclipse" src="https://img.shields.io/badge/eclipse%20ide-%232C2255.svg?&style=plastic&logo=eclipse%20ide&logoColor=white" /></a>
</p>

 ### <picture> <img src = "https://github.com/7oSkaaa/7oSkaaa/blob/main/Images/CP_PS.gif?raw=true" width = 50px>  </picture> Competitive Programming & Problem Solving
 
<p align="center">
  &emsp;
    <a href="#"><img alt = "Codeforces" src="https://img.shields.io/badge/codeforces%20-%231F8ACB.svg?style=plastic&logo=codeforces&logoColor=white" /></a>	
  &emsp;
    <a href="#"><img alt = "Leetcode" src="https://img.shields.io/badge/leetcode%20-%23FFA116.svg?style=plastic&logo=leetcode&logoColor=black" /></a>
  &emsp;
    <a href="#"><img alt = "Huckerrank" src="https://img.shields.io/badge/hackerrank-%232EC866.svg?style=plastic&logo=hackerrank&logoColor=white" /></a>
  &emsp;
    <a href="#"><img alt = "CodeChef" src="https://img.shields.io/badge/codechef-%235B4638.svg?style=plastic&logo=codechef&logoColor=white" /></a>
  &emsp;
    <a href="#"><img alt = "Google" src="https://img.shields.io/badge/google-%234285F4.svg?style=plastic&logo=google&logoColor=white" /></a>
  &emsp;
    <a href="#"><img alt = "Codin Game" src="https://img.shields.io/badge/codingame-%23F2BB13.svg?&style=plastic&logo=codingame&logoColor=black" /></a>
</p>

 ### <picture> <img src = "https://github.com/7oSkaaa/7oSkaaa/blob/main/Images/OS.gif?raw=true" width = 50px>  </picture> Operating Systems
 
<p align="center">
  &emsp;
    <a href="#"><img src="https://img.shields.io/badge/Linux-FCC624?style=plastic&logo=linux&logoColor=black"></a>
  &emsp;
    <a href="#"><img src="https://img.shields.io/badge/Ubuntu-E95420?style=plastic&logo=ubuntu&logoColor=white"></a>
  &emsp;
    <a href="#"><img src="https://img.shields.io/badge/Windows-0078D6?style=plastic&logo=windows&logoColor=white"></a>
  &emsp;
    <a href="#"><img src="https://img.shields.io/badge/pop!_os-%2348B9C7.svg?style=plastic&&logo=pop!_os&logoColor=white" /></a>
  &emsp;
    <a href="#"><img src="https://img.shields.io/badge/manjaro-%2335BF5C.svg?&style=plastic&logo=manjaro&logoColor=white" /></a>
</p>

<br> 

---

<p align = "center">
	<a href="https://github.com/piyushsuthar/github-readme-quotes"> <img alt = "Quote" src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight&animation=grow_out_in&quoteCategory=programming">
</p>

## <picture> <img src = "https://github.com/7oSkaaa/7oSkaaa/blob/main/Images/Statistics.gif?raw=true" width = 50px>  </picture> Github Stats

<details><summary><h3> 🔥 Streak Stats</h3></summary>

----	

<p align="center"><img src="https://github-readme-streak-stats.herokuapp.com/?user=7oSkaaa&theme=tokyonight_duo" alt="7oSkaaa" /></p>

</details>
  
<details><summary><h3>💻 GitHub Profile Stats</h3></summary>

----
	
<p align="center">
    <a href="https://github.com/anuraghazra/github-readme-stats">
	    <img alt="7oSkaaa's Github Stats" src="https://github-readme-stats.vercel.app/api?username=7oSkaaa&show_icons=true&count_private=true&locale=en&theme=tokyonight&layout=compact" height="230px"/></a>
	  <img src="https://github-readme-stats.vercel.app/api/top-langs?username=7oSkaaa&langs_count=10&show_icons=true&locale=en&theme=tokyonight" alt="7oSkaaa" height="230px"/>
<br/>

  <b>Note:</b> Top languages is only a metric of the languages my public code consists of and doesn't reflect experience or skill level.
  </p>
</details>

<details><summary><h3>⚡ Recent GitHub Activity</h3></summary>

----
	
[![7oSkaa's github activity graph](https://github-readme-activity-graph.cyclic.app/graph?username=7oSkaaa&theme=github	)](https://github.com/7oSkaaa/github-readme-activity-graph)

 
</details>

<details><summary> <h3> :trophy: Git profile Trophies </h3></summary>

----
	
<p align="center"> <a href="https://github.com/ryo-ma/github-profile-trophy"><img src="https://github-profile-trophy.vercel.app/?username=7oskaaa&layout=compact&theme=tokyonight&column=4&margin-w=15&margin-h=15" alt="7oskaaa" /></a> </p>

[![@7oskaa's Holopin board](https://holopin.io/api/user/board?user=7oskaa)](https://holopin.io/@7oskaa)
	
</details>
	
<details><summary><h3> :open_file_folder: My Repositories </h3></summary>

----
	
<div>
  <p align="center">
	<a href="https://github.com/7oSkaaa/LeetCode_DailyChallenge_2023">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=LeetCode_DailyChallenge_2023&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/Ahmed-Hossam">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=Ahmed-Hossam&theme=tokyonight" alt="GitHub Stats" />
    	</a>
    	<a href="https://github.com/7oSkaaa/Strees_Testing">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=Strees_Testing&theme=tokyonight" alt="GitHub Stats" />
    	</a>
    	<a href="https://github.com/7oSkaaa/CP-Templates">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=CP-Templates&theme=tokyonight" alt="GitHub Stats" />
    	</a>
    	<a href="https://github.com/7oSkaaa/Codeforces-Polygon-Template">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=Codeforces-Polygon-Template&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/Some-Linux-Commands">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=Some-Linux-Commands&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/Shorten-Link">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=Shorten-Link&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/7oSkaaa">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=7oSkaaa&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/Competitive-Programming-Session-Content">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=Competitive-Programming-Session-Content&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/VS-Code-for-CP">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=VS-Code-for-CP&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/Sorting-Algorithms">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=Sorting-Algorithms&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/board-link-generator">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=board-link-generator&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/Tic-Tac-Toe-GUI">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=Tic-Tac-Toe-GUI&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/PhoneBook-System">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=PhoneBook-System&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/Codeforces-Sheet-Generator">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=Codeforces-Sheet-Generator&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/CP-Calendar">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=CP-Calendar&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/Codeforces-Friends-Script">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=Codeforces-Friends-Script&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/vJudge-Board-Scrapper">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=vJudge-Board-Scrapper&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/CP-Templates-Snippets">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=CP-Templates-Snippets&theme=tokyonight" alt="GitHub Stats" />
    	</a>
	<a href="https://github.com/7oSkaaa/Udemy-Website">
      		<img src="https://github-readme-stats.vercel.app/api/pin/?username=7oSkaaa&repo=Udemy-Website&theme=tokyonight" alt="GitHub Stats" />
    	</a>
  </p>
</div>
</details>

</br></br>
	
## 🐍 A Snake Eating my Contributions Graph
	
<p align = "center">
	<img src = "https://github.com/7oSkaaa/7oSkaaa/blob/output/github-contribution-grid-snake.svg?" alt = "Snake Game"/>
</p>


