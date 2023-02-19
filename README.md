# RoboticDIMM
A fully automated DIMM seeing monitor is developed at the Indian Astronomical Observatory. It employs a 12 inch Meade telescope, a 72fps Lucid CMOS camera and a webcam based pointing setup. For automated/robotic operation, python scripts are running on an Adlink embedded computer.
![Picture1](https://user-images.githubusercontent.com/58334054/202841506-8e4ac09c-830b-4802-a5a1-7524fd17fef0.png)



<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/FxL5qM0.jpg" alt="Bot logo"></a>
</p>

<h3 align="center">Bot Name</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![Platform](https://img.shields.io/badge/platform-reddit-orange.svg)](https://www.reddit.com/user/Wordbook_Bot)
  [![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 🤖 Few lines describing what your bot does.
    <br> 
</p>

## 📝 Table of Contents
+ [About](#about)
+ [Demo / Working](#demo)
+ [How it works](#working)
+ [Usage](#usage)
+ [Getting Started](#getting_started)
+ [Deploying your own bot](#deployment)
+ [Built Using](#built_using)
+ [TODO](../TODO.md)
+ [Contributing](../CONTRIBUTING.md)
+ [Authors](#authors)
+ [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>
Write about 1-2 paragraphs describing the purpose of your bot.

## 🎥 Demo / Working <a name = "demo"></a>
![Working](https://media.giphy.com/media/20NLMBm0BkUOwNljwv/giphy.gif)

## 💭 How it works <a name = "working"></a>

The bot first extracts the word from the comment and then fetches word definitions, part of speech, example and source from the Oxford Dictionary API.

If the word does not exist in the Oxford Dictionary, the Oxford API then returns a 404 response upon which the bot then tries to fetch results form the Urban Dictionary API.

The bot uses the Pushshift API to fetch comments, PRAW module to reply to comments and Heroku as a server.

The entire bot is written in Python 3.6

## 🎈 Usage <a name = "usage"></a>

To use the bot, type:
```
!dict word
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
