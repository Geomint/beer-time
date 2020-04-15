######

# Beer Time! 🍻

** insert device screenshot **

Welcome to Beer Time, if you're like me then you love to drink beer, and not just the basic stuff, explore the wide range of variety using this website and make sure to add your favourites to your personal list. If you would like to get in touch about this project head over to my GitHub contact details.

## Contents: 

- UX 👍
    - Project Goals
    - Target Audience Goals
    - Site Owner Goals
    - User Stories
    - User Requirements and Expectations
- Design Choices 🎨
    - Fonts
    - Icons
    - Colours
    - Styling
    - Images
    - Backgrounds
- Planning✏️
- Wireframes 🔧
    - Website Layout
    - Account Creation Flowchart
    - Database Design
- Features 🎡
    - Features that have been developed
    - Features that will be implemented in the future
- Technologies Used 👨‍💻
- Testing + Planning: ✏️ 🔌
- Bugs 🐞
- Deployment 🚀
- Credits 💳

## User Experience: 👍

### Project Goals:
### Target Audience Goals:
### Site Owner Goals:
### User Stories:
### User Requirements and Expectations:


## Design Choices: 🎨

### Fonts:
### Icons:
### Colours:
### Base Styles:
### Images:
### Background (images/colours):

## Wireframes/Flowcharts: 🔧
 
### Website Layout:
### Account Creation Flowchart:
### Database Design:

## Features: 🎡

### Features that have been developed:
### Features that will be developed in the future:

## Technologies Used: 👨‍💻
#### Languages:
* <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a>
* <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">CSS</a>
* <a href="https://www.w3schools.com/js/">JavaScript</a>
* <a href="https://www.json.org/json-en.html">JSON</a>
* <a href="https://www.python.org/">Python</a>

#### Tools & Libraries: 

* <a href="https://jquery.com/">jQuery</a>
* <a href="https://git-scm.com/">Git</a>
* <a href="https://getbootstrap.com/">Bootstrap</a>
* <a href="https://fontawesome.com/icons?d=gallery">Font-Awesome</a>
* <a href="https://developers.google.com/maps/documentation/javascript/tutorial">Google Maps</a>
* <a href="https://kenwheeler.github.io/slick/">Slick Carousel</a>
* <a href="https://gulpjs.com/">Gulp.js</a>
* <a href="https://sass-lang.com/">SASS/SCSS</a>
* <a href="https://tinypng.com/">TinyPng (image compression)</a>

## Planning:  + Testing: ✏️ 🔌

#### Planning: 
Planning for this project took a significant amount of a time as to not skip over any detail, when using new languages I would argue that planning is THE most important aspect so that you don't miss something down the line.

#### Testing: 
This project naturally will need alot of testing due to the scope of the website, therefore my testing plan and documentation had to be very detailed with high levels of scrutiny. Due to the way the website was built I could perform and deploy tests in an organised fashion, page by page, feature by feature. 

#### Feature Testing 🎡: 

<strong>Sliding Banner -</strong>
- <strong>Plan</strong> 📝: I want to include a sliding banner on the project on multiple pages, but also with varying images/size depending on what page the user is currently on. I will need to choose images the represent the theme of the website and that also work well for a sliding banner with content on, I may add a dark overlay on the sliding banner so that content is easier to read.

- <strong>Implementation</strong> 🏭: Using slick.js carousel and the documentation provided (see credits) implementing this feature was simple, also having used this tool alot i'm familiar with the structure. Using conditional statements thanks to Flask and Jinja frameworks I was able to make the slider dynamic and render different content based on the page the user is currently on.

- <strong>Test</strong> 🧪: To test this feature I had to check that the slider rendered correctly on each page specified and also on each device size too, thanks to chrome-dev-tools this wasn't that much of a challenge. 

- <strong>Result</strong> 🏆: The test passed on all fronts, the content displayed was correctly aligned with that specified in the conditional statement. Also the speed of the slide works as intended.

- <strong>Verdict</strong> ✅: This test has passed based on the above criteria and notes.

## Bugs 🐞

#### Bugs During Development: 

<p>During development of this project, I face a few puzzling bugs that proved to be somewhat challenging, being new to Flask, Python etc means that it took me 
somewhat longer to find soltuions and fixes.</p>

<p>Case Sensitive Confusion:</p>

- <strong>Bug</strong> 🐞: <p>The code that handles the creation and and registration of the user accounts on BeerTime captures the inputted data and then transforms that into lowercase to then store into the database, the code that checks to see what current user was in session was throwing errors because it WAS looking for a case sensitive value.</p>
 
- <strong>Fix</strong> 🔧: <p>Altered the code so that it is no longer case sensitive when determining which user is currently active or in session on the website.</p>

- <strong>Verdict</strong> ✅: <p>This bug was squashed and meant I could continue working on other aspects of the project.</p>

#### Known Bugs: 


## Deployment 🚀

## Credits 💳



