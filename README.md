# Recipes for Calm - Introduction

Recipes for Calm is my 4th project with Code Institute and is a Full Stack website using the Django framework. It is designed as a website for users to find short blog posts with information on creating more calm in life. When a user is logged into the site they can like or unlike posts and comment on posts. They can edit or delete their own posts also. 

[Live Project Here](https)

![Website](./assets/readme_images/responsive.png)

## Content

  - [User Experience - UX](#user-experience---ux)
    - [User Stories](#user-stories)
    - [Agile Methodology](#agile-methodology)
    - [The Scope](#the-scope)
      - [Main Site Goals](#main-site-goals)
  - [Design](#design)
      - [Colours](#colours)
      - [Typography](#typography)
      - [Imagery](#imagery)
  - [Database Diagram](#database-diagram)
  - [Features](#features)
    - [Home Page](#home-page)
    - [Post Detail Page](#post-detail-page)
    - [Post Detail Page - Comments](#post-detail-page---comments)
    - [Edit Comments Page](#edit-comments-page)
    - [Search Box](#search-box)
    - [Search Results Page](#search-results-page)
    - [Search Results - No Results Found](#search-results---no-results-found)
    - [Signup Page](#signup-page)
    - [Login Page](#login-page)
    - [Logout Page](#logout-page)
    - [Navbar](#navbar)
    - [Footer](#footer)
  - [Admin Panel/Superuser](#admin-panelsuperuser)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
      - [Django Packages](#django-packages)
    - [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
    - [Testing](#testing)
  - [Creating the Django app](#creating-the-django-app)
  - [Deployment of This Project](#deployment-of-this-project)
  - [Final Deployment](#final-deployment)
  - [Forking This Project](#forking-this-project)
  - [Cloning This Project](#cloning-this-project)
  - [Credits](#credits)
    - [Content](#content)
    - [Information Sources / Resources](#information-sources--resources)
  - [Special Thanks](#special-thanks)

## User Experience - UX

### User Stories

* As a website user, I can:

1. Navigate the site and view content.
2. View a list of posts and choose accordingly.
3. Click on post to read the details.
4. Register for an account or login if I already have an account.
6. View the number of likes and comments on a post.
7. Read user comments on each post.

* As logged in website user, I can:

1. Like/unlike posts to indicate which I enjoyed.
2. Comment on posts to join coversation around the post.
3. Delete and edit my own comments.
4. Logout from the website.

* As a website superuser, I can:

1. Create and publish posts.
2. Create and review draft posts.
3. Approve and delete user comments.

### Agile Methodology

GitHub Projects were used to manage development of the project and can be found
[here](https://github.com/users/lauralola/projects/3)

### The Scope

#### Main Site Goals

* To provide users with a easy to use, well designed and attractive website with content for creating calm.
* To provide a clear purpose evident from first use of the website.
* To provide different leveles of access and interactions with the website based on permissions.
* To provide ways for users to interact with the content through likes and comments.

## Design

#### Colours

* The colour scheme is kept simple using muted green and grey tones throughout. This was also used to provide clear visibility of content as the user navigates the website. The background is kept a pale grey colour with a darker grey text used. The navigation uses a dark grey background with a pale green text to select pages. Buttons use a pale pink colour to highlight and hovering over links to full blog posts highlights in a bright green colour. 

#### Typography

* The Open Sans font is used as the main font for the whole project and the sans Serif font as a backup font. This was for consistency throughout the site and readability for users. 

#### Imagery

* There is only one static image used for the site as the homepage background. All other images are uploaded via Cloudinary to the database.


## Database Diagram

![Database Diagram](./assets/readme/)<br>

## Features

### Home Page

![Home Page](./assets/readme_images/home.png)
![Home Page2](./assets/readme_images/home_2.png)

* The hero image welcomes the user with a short message advertising what the website is about. The navigation links are clearly evident along the top and beneath the hero image are small exerpts from posts with a link to see in detail. These are limited to 6 per page and are updated by most recent post<br>


### Post Detail Page

![Post Detail Page](./assets/readme_images/post_detail.png)

* On selecting a post to view, users are brought to a page with the full post for them to read. The image linked with the post is displayed at the top of the page, along with the author and date of publication.  Here users can comment and like and unlike posts once they are logged in. The number of comments and likes is also shown<br>


### Post Detail Page - Comments

![Post Detail Page - Comments](./assets/readme_images/comment.png) 

* At the bottom of detailed post page, users can read the comments posted by other users. If the user is logged in or is a 
superuser they have access to the buttons for deleting or updating comments.

### Edit Comments Page

![Edit Comments Page](./assets/readme_images/logged_in_comment.png)

* If a user is logged in they can click a link beside their own comments and they are allowed to add, edit or delete their own comments. The website superuser can delete or update any comments on the blog without having to access the admin panel.

### Signup Page

![Signup Page](./assets/readme_images/sign_up.png)

* The new user is guided to complete a short form to access an account for further permissions on the site. Password length and complexity must be met. A message appears to confirm the user has been created and is logged in on successful account creation. 

### Login Page

![Login Page](./assets/readme_images/sign_in.png)

* Registered users can login to the site using their registered username and password. A message appears to confirm successful login. 

### Logout Page

![Logout Page](./assets/readme_images/sign_out.png)

* Users confirm that they wish to logout and recieve a message pop up to confirm logout.

### Navbar

![Navbar](./assets/readme_images/navbar.png)

* The navigation bar is present at the top of every page and houses all links to the various other pages.
* The options to Register or Log in will change to the option to log out once a user has logged in.
* The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes smaller.

### Footer

![Footer](./assets/readme_images/footer.png)
* The footer contains links to all social media for the page. 

## Admin Panel/Superuser
![Admin Panel](./assets/readme_images/admin.png)

* The admin panel allows superusers to view, create, edit and delete: 
1. Posts
2. Comments
3. Users
4. Email addresses

* Superusers can approve or delete comments by users. ![Admin Comment](./assets/readme_images/admin_comment.png) <br>

## Technologies Used

### Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML/)
* [CSS 3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://www.javascript.com/)
* [Django](https://www.python.org/)
* [Python](https://www.djangoproject.com/)

#### Django Packages

* [Gunicorn](https://gunicorn.org/)<br>
   As the server for Heroku
* [Cloudinary](https://cloudinary.com/)<br>
   Was used to host the static files and media
* [Dj_database_url](https://pypi.org/project/dj-database-url/)<br>
   To parse the database URL from the environment variables in Heroku
* [Psycopg2](https://pypi.org/project/psycopg2/)<br>
   As an adaptor for Python and PostgreSQL databases
* [Summernote](https://summernote.org/)<br>
   As a text editor
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)<br>
   For authentication, registration, account
   management
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)<br>
   To style the forms

### Frameworks - Libraries - Programs Used

* [Git](https://git-scm.com/)<br>
   Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub
* [GitHub](https://github.com/)<br>
   GitHub is used to store the project's code after being pushed from Git
* [Heroku](https://id.heroku.com)<br>
   Heroku was used to deploy the live project
* [PostgreSQL](https://www.postgresql.org/)<br>
   Database used through heroku.
* [Lucidchart](https://lucid.app/)<br>
   Lucidchart was used to create the database diagram
* [PEP8](http://pep8online.com/)<br>
   PEP8 was used to validate all the Python code
* [W3C - HTML](https://validator.w3.org/)<br>
   W3C- HTML was used to validate all the HTML code
* [W3C - CSS](https://jigsaw.w3.org/css-validator/)<br>
   W3C - CSS was used to validate the CSS code
* [Fontawesome](https://fontawesome.com/)<br>
   To add icons to the website
* [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)<br>
   To check App responsiveness and debugging
* [Google Fonts](https://fonts.google.com/)<br>
   To add the 2 fonts that were used throughout the project
* [Balsamiq](https://balsamiq.com/)<br>
   To build the wireframes for the project

### Testing

# Testing

* Testing was performed throughout the project. With new features added these were tested to ensure they were working as expected and if not debugging took place to try and recify the issue. 

### Python Validation - PEP8
* Python testing was done using the PEP8 Online to ensure there were no syntax errors in the project. All python files
were entered into the online checker and no errors were found in any of the custom codes.

### Lighthouse
Lighthouse was used to test Performance, Best Practices, Accessibility and SEO on Desktop.

##### Desktop Results:
![Lighthouse Mobile Result](./assets/readme/test/tasty_blog_lighthouse_desktop_results.jpg).

###### Mobile Results:
![Lighthouse Desktop Result](./assets/readme/test/tasty_blog_lighthouse_mobile_results.jpg).

### HTML Validation
![HTML Validation Result](./assets/readme/test/tasty_blog_html_validator_results.jpg).

### CSS Validation

![CSS Validation Result](./assets/readme/test/tasty_blog_css_validator_results.jpg).
![CSS Validation Result](./assets/readme/test/tasty_blog_css_validator_results_warnings.jpg).
* Custom CSS was validated using W3C Jigsaw validation service. Forty-three warnings were displayed, however, 
  these are related to Google Fonts and vendor extension prefixes which will not affect the CSS performance.

### JavaScript Validation
![CSS Validation Result](./assets/readme/test/tasty_blog_js_validator_results.jpg).

### jQuery Validation
![CSS Validation Result](./assets/readme/test/tasty_blog_jquery_validator_results.jpg).

### Console Results:
![Console Result](./assets/readme/test/tasty_blog_console_results.jpg).
* The browser console is clean, no errors are  showing.

## Manual Testing
### Frontend
* The Signup, Login and Logout system has no issues and is working accordingly. It shows the right 
  interactive message to the users.
* The Profile Page is working properly. It updates the user information and uploads/updates the 
  user profile image. It shows the interactive message to the user once the update is complete.
* The user profile image in the navbar and Post Details page has no issues and shows the user image 
  when it is uploaded by the user on the Profile Page.
* All the internal links are working and bring the user to the right page on the website.
* All the external links are working and bring the user to the right social media page by 
  opening a new browser tab.
* The Categories Page shows the recipes filtered by category without issues.
* The drop-down menu in the navbar shows a list of categories on every page of the website.
* The contact form on the Contact Page is working without any errors.  It sends an email, 
  to the info@tastyblog, once the user fills in the form and clicks on the send button. 
  Both interactive messages for email success or failure are also displayed on the screen.
* The pagination system is working. It adds another page after 6 posts on the page.
* On the Post Details Page, the Like/unlike functionality is working without issues and shows 
  the right interactive message to the user when the heart icon is clicked.
* The comment form has no issues and it submits a new comment once the form is completed by a
  registered user. 
  The comment is displayed once the submit button is pressed. The two interactive messages for 
  this action are working without errors. 
* The functionality to delete a message, previously sent by the user or by the superuser, is 
  working without issues. The Bootstrap model is open to asking the user if they want to delete 
  the message. Once the action is complete, the interactive message is displayed at the top of the page.
* The functionality to update a message, previously sent by the user or by the superuser, is 
  working without issues. A new page is open, to update the comment when the button edit is 
  pressed. Once the action is complete, the interactive message is displayed at the top of the page. 
* On the Books Page, the CRUD functionality is working without issues. Logged in users can create a new 
  post such as update or delete their own posts, also any post can be updated or deleted on this page by the Superuser.  

### Backend/Admin Panel
* I have tested the Admin Panel repeatedly since the start of the project development. All the models are working without issues.  
  I have created, deleted, and updated data in all models without errors. The models have the behavior expected for what they were built for.
* Whenever a user comments on a post or submits a book post the Superuser has to approve it before it will be displayed on the website. This functionality is 
  working without issues.
* When the author is posting a new recipe all the required fields have to be filled otherwise the author can't submit the post to the database.

### Manual Test Case
The Test case for this project can be found [here](TEST_CASE.md)

## Bugs
### Terminal Bug
#### Comment Model 
![Comment Model](./assets/readme/extras/comments_model_issue.jpg)
#### Terminal Error
![Comment Model - Terminal](./assets/readme/extras/terminal_comment_model_issue.jpg)

* While I was developing the project I tried to add a comment profile Image to the comments model by adding a 
  foreign key related to the profile model. When I was doing the migrations, the terminal required a default 
  number for the new foreign key.  I added the number zero however this was not the correct default option. 
  When I ran the migrations I got an error message on the terminal, saying that "(post_id)=(7) is not present in the table".

### Fixed Bug

* I spent a considerable amount of time trying to rectify this error. I sought advice from my slack community colleagues and researched 
  an online solution. I then called the Code Institute Tutor Assistance. I was advised, by the tutor, to reset my database on Heroku and 
  then run migrate on the terminal. I followed the advice and I fixed the issue by resetting my project database.

## Creating the Django app

1. Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click on Use This Template
3. Once the template is available in your repository click on Gitpod
4. When the image for the template and the Gitpod are ready open a new terminal to start a new Django App
5. Install Django and gunicorn: `pip3 install django gunicorn`
6. Install supporting database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url psycopg2`
7. Create file for requirements: in the terminal window type `pip freeze --local > requirements.txt`
8. Create project: in the terminal window type django-admin startproject your_project_name
9. Create app: in the terminal window type python3 manage.py startapp your_app_name
10. Add app to the list of installed apps in settings.py file: you_app_name
11. Migrate changes: in the terminal window type python3 manage.py migrate
12. Run the server to test if the app is installed, in the terminal window type python3 manage.py runserver
13. If the app has been installed correctly the window will display The install worked successfully! Congratulations!

## Deployment of This Project

* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New
App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. Click in resources and select Heroku Postgres database
7. Click Reveal Config Vars and add a new record with SECRET_KEY
8. Click Reveal Config Vars and add a new record with the `CLOUDINARY_URL`
9. Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1`
10. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
11. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
12. Scroll to the top of the page and choose the Deploy tab
13. Select Github as the deployment method
14. Confirm you want to connect to GitHub
15. Search for the repository name and click the connect button
16. Scroll to the bottom of the deploy page and select the preferred deployment type
17. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

## Final Deployment 

1. Create a runtime.txt `python-3.8.13`
2. Create a Procfile `web: gunicorn your_project_name.wsgi`
3. When development is complete change the debug setting to: `DEBUG = False` in settings.py
4. In this project the summernote editor was used so for this to work in Heroku add: `X_FRAME_OPTIONS = SAMEORIGIN `to
   settings.py.
5. In Heroku settings, delete the config vars for `DISABLE_COLLECTSTATIC = 1`

## Forking This Project

* Fork this project by following the steps:

1. Open [GitHub](https://github.com/PedroCristo/portfolio_project_4)
2. Find the 'Fork' button at the top right of the page
3. Once you click the button the fork will be in your repository

## Cloning This Project

* Clone this project by following the steps:

1. Open [GitHub](https://github.com/PedroCristo/portfolio_project_4)
2. You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order
to copy the URL
3. Once you click the button the fork will be in your repository
4. Open a new terminal
5. Change the current working directory to the location that you want the cloned directory
6. Type 'git clone' and paste the URL copied in step 3
7. Press 'Enter' and the project is cloned

## Credits

### Content

* All food recipes were taken from [BBC Goodfood](https://www.bbcgoodfood.com/recipes)
* The cookbook’s information and images were sourced from [Eason’s](https://www.easons.com/)
* The images were taken from [Unsplash](https://unsplash.com/)
* The Tasty Blog logos and favicon are my own design and build

### Information Sources / Resources

* [W3Schools - Python](https://www.w3schools.com/python/)
* [Stack Overflow](https://stackoverflow.com/)
* [Scrimba - Pyhton](https://scrimba.com/learn/python)

## Special Thanks

* Special thanks to my mentor Sandeep Aggarwal, my colleagues at Code Institute, Kasia Bogucka, and Mairéad Gillic for
their assistance throughout this project.