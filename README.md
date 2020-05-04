######

# Beer Time! 🍻

** insert device screenshot **

<img src="https://github.com/Geomint/beer-time/raw/master/wireframes/screenshot/multi-device.png?raw=true"></img>

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
	- Deploying to Heroku
    - Locally run this project
- Credits 💳

## User Experience: 👍

### Project Goals:
The goal of this project is to showcase various types of craft ales for those who enjoy the experimentation in the brewing process. The users who access to website will be able to create a favourites list from a list of products. This website is not aimed at people who are under the suitable age to consume alchohol.

### Target Audience Goals:
- To be able to find out information about various craft beverages.
- Create an account and build up a favourites list to keep track of the beers they have tasted.
- A visually inviting and appealing design.
- A facility to send messages to the company to discuss the beverages.
- To be able to consume the information on the website on Desktop/Tablet and mobile devices.

### Site Owner Goals:
- Generate increased interest for various branded beverages.
- Collect user information in terms of site analytics.
- Recieve messages from the users to interact with.
- Attract branded beverages to feature on the website.

### User Stories:

### User Requirements and Expectations:

#### Requirements:
- Interact with a visually appealing website.
- Navigate the website with ease & with fast load times.
- Extract information on various craft beverages.
- Information on the website to be laid out in a clear and effective way.
- Construct a list of beverages to try, or to remember.
#### Expectations:
- The website protects the users information.
- The users can interact with the elements visible on the page.
- The website loads with sufficient speed.
- The content on the website renders correctly on desktop, mobile and tablet.
- The users feel informed and satisfied with the informaton available.

## Design Choices: 🎨
The design of this website had to reflect the theme of craft beverages, therefore using a rustic font and bold colours were a must. I believe the choices I have made make an intruiging and sophisticated blend and both complete a design the users will likely interact with on a positive level.

### Fonts:
I chose to use two font families, one for the Titles on the website and another for the content, i.e paragraphs, descriptions etc.

#### Heading-font:
I chose to use the 'Permanent Marker' font for the titles on this project as it encapsulates the chalk on a black board look, which is perfect for this theme. With the main focus on showcasing beverages that often have been started by a few people experimenting, I thought this rustic, creative looking font really did the trick.

#### Content-font: 
I chose to use the 'Roboto Mono' font for the content on the website, it provides an elegant yet clear layout for the content on the website.

### Icons:
Utilising the vast array of icons from font-awesome I was easily able to locate the icons I needed to provide the best user experience for those interacting with the site.
### Colours:
The colours I chose to use for this website provide a visually captivating experience for the users, provoking a positive response using bright colours will potentially increase the interaction levels on the website.

- Primary: #1B443A 'msu-green' This green provides a bold structural aspect to the website and defines the borders of the web page.
- Secondary: #ffc038 'winter-orange' The yellow/orange colour used on the website contrasts elegantly with the primary colour and provides a clear option to use on elements like navigaton links.
- Default body color: #E3E4DB 'platinum' This 'off-white' platinum colour provides a neutral backdrop for featured elements on the webpage, neatly highlighting the important aspects on the webpage and drawing the users attention.
- Error colour: #FFCCCC 'error' This standard error colour is a slightly muted red in order to not provoke too much of a negative response, but to still indicate to the user that someone didn't work as intended.
- Success colour: #4BB543 'success' The success colour is similarly a muted green, however the selection behind this colour was more influenced by how visually appealing the contrast is between that and the main backdrop of the webpage.
- White colour: #FFF 'white' Standard white colour. 
- Red color: #ff0000 'red' Standard red colour.
- Black colour: #000 'black' Standard black colour.
### Base Styles:
Colours:
```
$primary-color: #1B443A; // msu-green
$secondary-color: #ffc038; // winter-orange
$default-body-color: #E3E4DB; // platinum
$error-color: #FFCCCC; // error
$success-color: #4BB543; //success
$white-color: #FFF; // white 
$red-color: #ff0000; // red
$black-color: #000; // black
```
Shadows:
```
$default-box-shadow: 1px 1px 1px rgba(0,0,0,0.5);
$darkest-box-shadow: 1px 1px 2px rgba(0,0,0,0.5);
$default-text-shadow: 1px 1px 1px rgba(0,0,0,0.5);
```
Transitions:
```
$default-transition: 0.15s ease-in-out;
```
### Images:
The images i've chosen to use on the website were selected to invite people into the website by looking appealing to those who are legally allowed to consume alcohol.
### Background Images:
The background images i've used on the sliding banner of the website were also selected to provide an instant context to the web page, the user knows what the theme of the page is just by looking at the banner, this also serves as a useful way to draw attention to the call to action buttons on the banners.

## Wireframes/Flowcharts: 🔧
I Built the wireframes for this project using Sketch, this software allowed me to easily construct a wireframe for multiple devices, and for all the pages and features I wanted to include on the project. Having these were useful to provide me with a blueprint of sorts to follow when writing the code for the website, having the design choices initially mapped out speeded up the process alltogether.

View the wireframes for this project <a href="https://github.com/Geomint/beer-time/tree/master/wireframes">here.</a>
 
### Account Creation Flowchart:
The account creation flowchart allowed me to understand the required logic in order to handle the creation and management of letting users create accounts on the website, this flowchart can be veiwed <a href="https://github.com/Geomint/beer-time/tree/master/wireframes/flowcharts">here.</a>
### Database Design:
Utilising the NoSQL features that MongoDB provides I was able to map out the following collections.

### Data Storage Types:
The types of data that are stored in the MongoDB database.
- ObjectID
- String
- Boolean
- Object
- Array
- Binary

Beers Collection:
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Beer Id|_id|ObjectId
Name|name|String
Brewery|brewery|String
Type|type|String
Excerpt|excerpt|String
Notes|notes|String
Abv|abv|String
Image|image|String
Reviews|reviews|Array

Types Collection:
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Type ID|_id|ObjectID
Beer Type|beer_type|String

Users Collection:
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
User ID|_id|ObjectID
Name|name|String
Password|password|Binary
Admin|admin|boolean
Favourites|favourites|array

View the schema templates for the database collections <a href="https://github.com/Geomint/beer-time/tree/master/data/schemas">here.</a>

## Features: 🎡

### Features that have been developed:
- Sliding banner to sit on various pages that provides additional call-to-action.
- Register an account form, Sign-in & Sign-out functionality.
- Add to favourites feature, allowing users to flag beverages as a 'favourite' and having them visible on their unique, 'my-list' page.
- Users can leave reviews on individual beers, edit their reviews, delete their reviews, and read what other people have to say.
- The webmaster has access to the 'add-beer', 'edit-beer' and delete beer pages & functions.

### Features that will be developed in the future:
- An option to purchase the products users can see on the website.
- Advanced product information, including maps leading users to the closest place they can taste the beverage.
- An option for users to opt-in to a mailing list to keep up to date with the latest from BeerTime.
- Email authentication to provide a second level of security.
- The ability to filter the beverages by type, abv% etc.

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



