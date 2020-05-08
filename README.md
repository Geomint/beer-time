# Beer Time! 🍻

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
- Planning + Testing: ✏️ 🔌
- Bugs 🐞
- Deployment 🚀
	- Deploying to Heroku
    - Locally run this project
- Credits 💳
- Disclaimer

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

Phil says:
"I've wanted to find a website that provides me with a list of craft beverages and all the info about them, it would be nice to be able to store these drinks on a list of some sort so I can keep track of which ones ive had!"

Mike says:
"Im looking for a tool that not only works on my computer but also on my phone so that i can access it when im out and about exploring cities."

John says:
"When I search for beers online im often bombarded with marketing promotions and offers, I want a clean elegant website that offers me the information i need" 

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
```scss
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
```scss
$default-box-shadow: 1px 1px 1px rgba(0,0,0,0.5);
$darkest-box-shadow: 1px 1px 2px rgba(0,0,0,0.5);
$default-text-shadow: 1px 1px 1px rgba(0,0,0,0.5);
```
Transitions:
```scss
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
- Use of AWS image CDNs to handle uploading images to add to beer 'products'.
- An option to purchase the products users can see on the website.
- Advanced product information, including maps leading users to the closest place they can taste the beverage.
- An option for users to opt-in to a mailing list to keep up to date with the latest from BeerTime🍻.
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
* <a href="https://kenwheeler.github.io/slick/">Slick Carousel</a>
* <a href="https://sass-lang.com/">SASS/SCSS</a>
* <a href="https://tinypng.com/">TinyPng (image compression)</a>
* <a href="https://www.mongodb.com/cloud/atlas">MongoDB Atlas</a>
* <a href="https://pymongo.readthedocs.io/en/stable/">PyMongo</a>
* <a href="https://flask.palletsprojects.com/en/1.0.x/">Flask</a>
* <a href="https://jinja.palletsprojects.com/en/2.10.x/">Jinja</a>

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

<strong>Create an account -</strong>
- <strong>Plan</strong> 📝: In order to meet the criteria of the project goals I needed to implement a way in that users on the website could create an account on the website that would then allow them to perform actions that manipulates or creates records within the collections in the MongDB. I needed to research the best ways to handle this feature in terms of making it easy for users to create an account and also properly hash the password when it is stored into the database.

- <strong>Implementation</strong> 🏭: Firstly importing session and bcrypt was required in order to efficiently handle the request. The code checks first that the passwords entered match so that the user does not make any typo mistake, after that the code checks to see if the username entered already exists in the database, using flash here to alert the user to any mistakes or issues they encounter when creating an account. Upon passing the prior tests the new user is passed into the users.collection as an object with the ‘name’ field and hashed password thanks to bcrypt. Then the code initiates the ‘session’ for the user signing them in.

- <strong>Test</strong> 🧪: To test this feature I had to create a few temporary accounts in order to test that the registration worked as intended, checking what values were passed & stored in the database.

- <strong>Result</strong> 🏆: The test passed as the created test user accounts stored in the database with encrypted passwords and the user was signed into session.

- <strong>Verdict</strong> ✅: This test has passed based on the above criteria and notes.

<strong>Sign into account -</strong>
- <strong>Plan</strong> 📝: I needed to build a page and function that allowed the users to sign in to their account that they made so they can access the information stored in their favourites array, and also have access to view all of the beers and information listed on beer time.

- <strong>Implementation</strong> 🏭: The code checks that the information from the request matches the information that is stored in the users collection, and if it does the session is made with the user, otherwise a flash is triggered letting the user know that there was an in issue with his/hers account details.
- <strong>Test</strong> 🧪: To test the sign in feature I first made a test account with username test123 and password test123 and attempted to sign in using this page.

- <strong>Result</strong> 🏆: The test passed as the session was made and i was signed into the account ‘test123’ i double checked this by checking the session cookie in dev-tools.

- <strong>Verdict</strong> ✅: This test has passed based on the above criteria and Notes.

<strong>Sign out of account -</strong>
- <strong>Plan</strong> 📝: There also needed to be a sign-out feature for the users so that they could sign out of their account if they so wished.

- <strong>Implementation</strong> 🏭: Creating a route and method for the sign-out functionality was relatively simple, using session.clear clears the active session.

- <strong>Test</strong> 🧪: Testing this feature was simple, all i had to do was sign into the previously created account and click the sign-out button in the navigation.

- <strong>Result</strong> 🏆: The test passed as the session was cleared out and the user was no longer signed in.

- <strong>Verdict</strong> ✅: This test has passed based on the above criteria and notes.

<strong>Add beer to favourites list -</strong>
- <strong>Plan</strong> 📝: I wanted to develop a way that the user could interact with the beers listed on the all-beers page, and therefore planned to create an add to favourites button, this would allow the user to read about the beer, decide whether or not they liked the sound of it and click the empty beer icon which would then fill the beer icon and add that objectid of that beer to the users favourites array, this would then be visible on the my-list page.

- <strong>Implementation</strong> 🏭: To implement this feature i created a form that would auto submit once the checkbox was checked using JavaScript, the beer_id which is unique and accessible in the jinja templates is then passed into the current users favourites array and stored in the mongoDB.

- <strong>Test</strong> 🧪: To test this feature worked i needed to submit the form and check the database to see if the objectID had been placed into the correct user that was signed in.

- <strong>Result</strong> 🏆: The objectID for the beer clicked successfully was entered into the favourites array of the test account.

- <strong>Verdict</strong> ✅: This test has passed based on the above criteria and notes.

<strong>My List page -</strong>
- <strong>Plan</strong> 📝: In order to utilise the add to favourites feature in more depth i wanted to create a page in which users could view all of the beers they had marked as favourite, creating a one stop place for them to check if they are out. I needed to make this page access the data of each beer using the objectID store in the favourites array of the current user.

- <strong>Implementation</strong> 🏭: To implement this feature i looped over each id in the current users favourites array, and then passed this data to the template where the beers in the users favourites array were generated.

- <strong>Test</strong> 🧪: Testing this feature was relatively simple, once the objectID was in the favourites array of the current user, the beer should appear on the my list page.

- <strong>Result</strong> 🏆: The beer appeared on the my list page individually which shows how only the selected objectID was passed into the favourites array of the current user.

- <strong>Verdict</strong> ✅: This test has passed based on the above criteria and notes.

<strong>Writing, Reading, Updating and Deleting a review of a beer -</strong>
- <strong>Plan</strong> 📝: This feature is largely the main focus in terms of demonstrating CRUD functionality that is user facing, I knew I would need to figure out an intuitive way that users
could post reviews on a specific beer, and only interact, as in update and delete, the ones that they had made. I planned at first to have this information stored against the beer inside the beer collection
but later created a review collection.

- <strong>Implementation</strong> 🏭: Once I had setup the reviews collection with the MongoDB database, I could start to contsruct the relevant code that would allow my users to interact with reviews, creating 4 routes for each 
step within the CRUD operation allowed me to neatly structure this feature.

- <strong>Test</strong> 🧪: Performing each step of CRUD on the review tool and checking the database to see if the changes we're being made correctly.

- <strong>Result</strong> 🏆: The intended changes were made and the database was updated accordingly.

- <strong>Verdict</strong> ✅: This test has passed based on the above criteria and notes.

<strong>All beers page -</strong>
- <strong>Plan</strong> 📝: I needed to create a page in which all the beers in the beers collection could be rendered, this would be done on the all-beers page, in order to interact with the add-to-favourites functionality im going to need this page to be accessible only when a user is in session.

- <strong>Implementation</strong> 🏭: Implementing this page + feature was relatively simple, i made the connection to the collection on the route and made the data available for the template, then i created a loop using Jinja and each beer rendered correctly.

- <strong>Test</strong> 🧪: To test if this feature worked i accessed the all-beers page and determined whether all the data was rendered correctly.

- <strong>Result</strong> 🏆: The data was rendered correctly and all the beers in the collection were pulled out.

- <strong>Verdict</strong> ✅: This test has passed based on the above criteria and notes.


## Bugs 🐞

#### Bugs During Development: 

<p>During development of this project, I face a few puzzling bugs that proved to be somewhat challenging, being new to Flask, Python etc means that it took me 
somewhat longer to find soltuions and fixes.</p>

<p>Case Sensitive Confusion:</p>

- <strong>Bug</strong> 🐞: <p>The code that handles the creation and and registration of the user accounts on BeerTime🍻 captures the inputted data and then transforms that into lowercase to then store into the database, the code that checks to see what current user was in session was throwing errors because it WAS looking for a case sensitive value.</p>
 
- <strong>Fix</strong> 🔧: <p>Altered the code so that it is no longer case sensitive when determining which user is currently active or in session on the website.</p>

- <strong>Verdict</strong> ✅: <p>This bug was squashed and meant I could continue working on other aspects of the project.</p>

<p>Favourites Array Issue:</p>

- <strong>Bug</strong> 🐞: <p>When the user adds or removes a beer from their 'my-list' or favourites array with multiple beers on the page, the last rendered beer on the page gets added or removed from the list.</p>
 
- <strong>Fix</strong> 🔧: <p>Altering the jQuery selector code fixed this issue and only submits the forms that are the relevant parents of the input.</p>

- <strong>Verdict</strong> ✅: <p>This bug was debugged, dealt with and moved on from.</p>

## Deployment 🚀

BeerTime🍻 was developed on Visual Studio Code, using git and GitHub to host the repository.

### Cloning BeerTime🍻 from GitHub:

<strong>Ensure</strong> you have the following installed:
* PIP
* Python 3
* Git

<strong>Make sure you have an account at <a href="https://www.mongodb.com/">MongoDB</a> in order to construct the database.</strong>

<em>WARNING: You may need to follow a different guide based on the OS you are using, read more <a href="https://python.readthedocs.io/en/latest/library/venv.html">here.</a></em>

* 1: <strong>Clone</strong> the BeerTime🍻 repository by either downloading from <a href="https://github.com/Geomint/beer-time"> here</a>, or if you have Git installed typing the following command into your terminal.
```bash
git clone https://github.com/geomint/beertime
```
* 2: <strong>Navigate</strong> to this folder in your terminal.
* 3: <strong>Enter</strong> the following command into your terminal.
```bash
python3 -m .venv venv
```
* 4: <strong>Initilaize</strong> the environment by using the following command.
```bash
.venv\bin\activate 
```
* 5: <strong>Install</strong> the relevant requirements & dependancies from the requirements.txt file.
```bash
pip3 -r requirements.txt
```
* 6: In your IDE now <strong>create</strong> a file where you can store your SECRET_KEY and your MONGO_URI, follow the schema structure located in data/schemas to properly setup the Mongo Collections.
<em>NOTE: I developed this website on Visual Studio Code and used the following settings.json file, delete and replace with your values.</em>
```json
{
    "python.pythonPath": "env/bin/python",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "python.linting.pylintArgs": ["--load-plugins=pylint_flask"],
    "files.autoSave": "onFocusChange",
    "files.useExperimentalFileWatcher": true,
    "terminal.integrated.env.osx": {
      "SECRET_KEY": "<your_secret_key>",
      "DEV": "1",
      "FLASK_DEBUG": "1",
      "MONGO_URI": "<your_mongo_uri>"
    }      
}
```
* 7: Run the application using 
```bash
flask run 
```
or 
```bash
Python3 app.py
```

### Deploying BeerTime🍻 to Heroku:

* 1: <strong>Create</strong> a requirements.txt file using the following command.
```bash
pip3 freeze > requirements.txt
```
* 2: <strong>Create</strong> a Procfile with the following command.
```bash
echo web: python3 app.py > Procfile
```
* 3: <strong>Push</strong> these newly created files to your repository.
* 4: <strong>Create</strong> a new app for this project on the Heroku Dashboard.
* 5: <strong>Select</strong> your <strong>deployment</strong> method by clicking on the <strong>deployment</strong> method button and select GitHub.
* 6: On the dashboard, <strong>set</strong> the following config variables:

**Key**|**Value**
:-----:|:-----:
IP|0.0.0.0
PORT|5000
MONGO\_URI|mongodb+srv://<username>:<password>@<cluster\_name>-qtxun.mongodb.net/<database\_name>?retryWrites=true&w=majority
SECRET\_KEY|"your\_secret\_key"
* 7: Click the deploy button on the Heroku dashboard.
* 8: The site has been deployed the Heroku.

## Credits 💳

* <a href="https://medium.com/developing-with-sass/creating-a-dead-simple-sass-mixin-to-handle-responsive-breakpoints-889927b37740">Mixin For Breakpoints</a>
* <a href="https://www.favicon-generator.org/">Favicon Generator</a>  
* <a href="https://coolors.co/">Coolors.co</a>
* <a href="https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB">Unicorn Revealer</a>

## Disclaimer
The contents of this website are for educational purposes only.


