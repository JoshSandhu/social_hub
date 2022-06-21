# Social Hub

# Table of Contents
* [Social Hub Introduction](#introduction-to-social-hub)
* [UX](#ux)
    + [Strategy](#strategy)
    + [Scope](#scope)
    + [Structure](#structure)
    + [Skeleton](#skeleton)
    + [Surface](#surface)
* [Features](#features)
* [Technologies Used](#technology-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

# Introduction to Social Hub
Welcome to Social Hub. The Full Stack Web Application for communites to grow. The ability to create posts and discussions to hear and converse any topic. To visit the final launched project click here!!!!!!!!

# UX
## Strategy
User expectations:
* The user should have the ability to create a post, see other users comments and likes as well as comment on own and/or other posts.

Target Audience:
* People who wish to share their thoughts of all ages and from all around the world.

User Stories:
* As a Site Admin I can create, read, update and delete posts so that I can manage my blog content.
* As a Site Admin I can review submitted posts before publication.
* As a Site Admin I can create draft posts so that I can finish writing the content later.
* As a Site User I can view a paginated list of posts so that easily select a post to view.
* As a Site user / Admin I can view post dislikes.
* As a Site user / Admin I can view the number of likes on each post so that see which is the most popular or viral.
* As a Site User I can click on a post so that read the full text.
* As a Site user / Admin I can view comments on an individual post so that read the conversation.
* As a Site User I can register an account so that I can comment and like.
* As a Site User I can leave comments on a post so that I can be involved in the conversation.
* As a Site user I can Create a post so that share my view with the world.
* As a Site User I can like or unlike a post so that I can interact with the content.

## Scope
### Content Requirements:
* Admin panel where the owner of the site can approve and manage comments.
* A page where user can register.
* A page where user can log in.
* A page where user can log out.
* A page which displays a list of posts written by users.
* A page where user can rad the content of a particular post.
* A page where user can create own post.

### Functional Requirements:
* Option for the owner to approve and manage posts.
* Option for the users to register at the website.
* Option for the users to log in to the website.
* Option for the users to log out from the website.
* Option for the users to see posts and choose to read it's content.
* Option for the users to read content of selected post.
* Option for the users to write a post.
* Option for the users to like or dislike posts.

## Structure
### Interaction Function Design
* Navbar to include all options in a presentable way for the user.
* Information alerting the user of any changes upon an action.
* Buttons placed throughout the website are easy to see and are clear in their function.

### Information Structure
* Simple design with clear and visible information presented to the user for easy use.
* Home page contains information which is clear in asking for registration to gain full access to the site.
* User is alerted with feedback on any changes made.
* Navigation shows clearly the current login status of the user.

## Skeleton
### Navigation
* When the Logo (Social Hub) is clicked the user is directed to the home page.
* When the Home button is clicked the user is directed to the home page.
* When the Register button is clicked the user is directed to the Sign up page.
* When the Log in button is clicked the user is directed to the Log in page.
* When the Log out button is clicked the user is directed to the Log out page.
* When the title for a post is clicked the user is taken to the post details page.
* When the User is logged in the navigation displays the logged in user name.

### Interface Design
All elements on the website needs to ensure ease of access, easy to understand and use in order to maximize usability and experience.

### Wireframes
Wireframes can be found <a href="https://github.com/JoshSandhu/social_hub/tree/main/assets/wireframes" target="_blank">here.</a>

## Surface
* All interface content arrangement, typography, navigation and colors have been designed for ease of use and a relaxed emotional use in mind.

# Features
## Existing:
* Ability to register on the website.
* Ability to login to a registered account.
* Ability to logout of an account.
* Ability to view other posts on the site.
* Ability to select and read a specific post.
* Ability to select and view a posts comments/likes/dislikes.
* Ability to create own post.
* Ability to like a post.
* Ability to dislike a post.
* Ability to comment on a post.

## Features left to implement:
* Ability to edit own posts.
* Ability to delete own posts.
* Ability to post more than one image.
* Ability to draft a post and save for later.
* Ability to report a post.

# Technology Used
* [HTML]
* [CSS]
* [Javascript]
* [Python]
* [Heroku] - Cloud platform for hosting applications.
* [PostgreSQL] - Relational database management system.
* [Django] - Python framework
* [Gunicorn] - Server used by Django to run on Heroku.
* [Dj Database Url] - Library for PostgreSQL
* [Psycopg2] - PostgreSQL database adapter for use with Python.
* [Dj3 Cloudinary Storage] - Django package for Cloudinary Storage.
* [Balsamiq](https://balsamiq.com) - Used to create wireframes.

# Testing
## Manual Testing:
Website functionality tested according to user stories:
### As the owner of the site:
| Goal | Achieved |
| --- | --- |
| To be able to approve the posts before they are presented on the site |  Yes |
|  |  |

The owner of the website can access the admin panel by adding /admin onto the end of homepage url.
There, the owner has to put in admin credentials provided by the developer.

### As a user of the site:
| Goal | Achieved |
| --- | --- |
| Able to register for an account for full access | Yes |
| Able to view all posts as a list for easy selection | Yes |
| Able to click on a post to view whole content and comments | Yes |
| Able to like/dislike a post | Yes |
| Able to leave a comment if user is logged in | Yes |
| Able to write a post and submit for publication | Yes |
|  |  |

### Feedback and alert message tests:
| Goal | Achieved |
| --- | --- |
| User informed of logged in status | Yes |
| User able to register for an account | Yes |
| User able to login to a account | Yes |
| User able to logout to a account | Yes |
| User submitted a post for publication | Yes |
| When creating a post the user is alerted when required fields are empty | Yes |
|  |  |

### Usability

After logging in or creating a post the user is diverted to the home page. User can only like/dislike and comment while logged in.

All buttons function as intended.

## Automatic Testing:

- https://validator.w3.org/ - used to validate HTML syntax
- https://jigsaw.w3.org/css-validator/ - used to validate CSS syntax
- https://esprima.org/demo/validate.html - used to validate Javascript syntax
- http://pep8online.com/ - used to validate Python syntax
- https://search.google.com/test/mobile-friendly - tested for mobile compatibility of the website
- https://pagespeed.web.dev/?utm_source=psi&utm_medium=redirect - tested for the websites loading speed performance

## Bugs

At time of deployment there was no known bugs found. 

# Deployment

## Initial Commit

Once I created the project, the app and installed Django and supporting libraries in Gitpod, I created the requirements.txt file with the following command, in terminal:
- pip install -r requirements.txt

Once logged into Heroku I:
* Created new Heroku App
* Added ‘Heroku Postgres’ database to App Resources
* Copied DATABASE_URL value from Config Vars, in the Settings Tab

In Gitpod, in newly created env.py file I:
* Imported os library
* Set environment variables - os.environ["DATABASE_URL"] to the url copied from Heroku
* Added in a secret key - os.environ["SECRET_KEY"] (Made up string of characters)

In Heroku I:
* Added the newly created secret key to Config Vars - SECRET_KEY

In settings.py I referenced env.py:
* import os
* import dj_database_url 
* if os.path.isfile("env.py"):
* import env
* Replace the secure key - SECRET_KEY = os.environ.get('<new secure key>')  
* Comment out the the old database section and added the new database section

In terminal I saved all changes and made migrations with the following command:
* python3 manage.py migrate

Once logged in, from Cloudinary website I:
* Copied CLOUDINARY_URL

In env.py I:
* Added Cloudinary URL to env.py

In Heroku I:
* Added Cloudinary URL to Heroku Config Vars
* Add DISABLE_COLLECTSTATIC to Heroku Config Vars and set it to 1 (It's only until the deployment)

In settings.py I:
* Added Cloudinary Libraries to installed apps
* Inserted code which tells Django to use Cloudinary to store media and static files
* Linked file to the templates directory in Heroku - TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Changed the templates directory to TEMPLATES_DIR
* Added Heroku Hostname to ALLOWED_HOSTS - ALLOWED_HOSTS = ["socialhub-p4.herokuapp.com", "localhost"]

In Gitpod I created 3 new folders in top level directory:
* media, static, templates

In Procfile I added the following code:
* web: gunicorn social_hub.wsgi

Due to a security issue, Heroku has disabled automated deployments from GitHub.  
In the Gitpod terminal, I typed:
* heroku login -i
* heroku apps
* heroku git:remote -a social_hub
* git add . && git commit -m "Deploy to Heroku via CLI"
To push changes to heroku I used the following command:
* git push heroku main

Before the final deployment, I changed the DEBUG to False in settings.py and removed the DISABLE_COLLECTSTATIC from config vars in Heroku.

# Credits

* Code Institute - For providing the base template in which to work from. HTML and CSS.
* Pexels.com - Photos which are used throughout the website.