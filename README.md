# Build your Dream
Build your dream is a imaginary blog where users can share their own pc builds, find inspiration from other builds and interact with other pc-builders. Here everyone can see what is out there before, during and after building your own computer. 

It is meant to be a place for people to exchange information and just show off their work. Hence the target audience are pc enthusiats who want to present their own build with helpful imformation for future pc builders and for those future pc-builders to get inspired by others work.
The post will have professional tags by the build-your-dream-team so that users can search through the contents by parts and characteristics they are looking for. Moreover users can express their feelings about a post via comments and a like function.

Moreover as this imaginary website is still new and wants to adapt to the users' needs, users can give recommendation of what changes and possible features they would implement on the blog. Therefore, Build Your Dream tries to build a growing community of builders that want to exchange information with one another in a respectful way.

[Build Your Dream - Deployed website](https://build-your-dream-87f4998d58a9.herokuapp.com/)

## Contents
- [SITE OWNER GOALS](#site-owner-goals)
- [USER EXPERIENCE (UX)](#user-experience-ux)
- [WIREFRAMES](#wireframes)
- [AGILE](#agile)
- [ENTITY RELATIONSHIP DIAGRAM - ERD](#entity-relationship-diagram---erd)
- [FINAL DESIGN](#final-design)
    - [Imagery](#imagery)
    - [Color Scheme](#color-scheme)
    - [Typography](#typography)
    - [Visual Effects](#visual-effects)
    - [Final Look](#final-look)
- [FEATURES](#features)
    - [Index Page](#index-page)
    - [Show Build Page](#-page)
    - [Search build via tags](#-page)
    - [Create Build Post](#-page)
    - [Edit Build Post](#-page)
    - [Delete Build Post](#-page)
    - [Future Content](#future-)
    - [404 Page](#404-page)
    - [403 Page](#403-page)
- [TESTING](#testing)
    - [Accessibility](#accessibility)
        - [Wave Testing](#wave-testing)
        - [Lighthouse Testing](#lighthouse-testing)
    - [W3C Validators](#w3c-validators)
    - [JSHint](#jshint)
    - [PEP8](#pep8)
    - [Form Testing](#form-testing)
    - [Links Testing](#links-testing)
    - [Browser Testing](#browser-testing)
    - [Device Testing](#device-testing)
    - [User Stories Testing](#user-stories-testing)
    - [Fixed Bugs](#fixed-bugs)
- [TECHNOLOGIES USED](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programs used](#frameworks-libraries-and-programs-used)
- [DEPLOYMENT](#deployment)
- [CREDITS](#credits)
    - [Media](#media)
    - [Resources](#resources)
- [ACKNOWLEDGEMENTS](#acknowledgements)


## SITE OWNER GOALS

- to provide the user with an informative website about pc builds
- to provide the user with the ability to become part of a community of pc builders
- to provide the user with the opportunity to upload, edit and delete their own pc build with information about it
- to provide the user with the opportunity to comment on ones own or others' pc builds, the comments can be edited and deleted
- to provide the user with the ability to search all posts via their tags
- to provide the user with the ability to show their appreciation of a post with likes
- to provide the user with the ability give input on what features the website could need and hence become a part of the development process
- to provide the user with a save space, where content is approved so bullying and other problematic behaviour is limited

## USER EXPERIENCE (UX)
#### First Time User Goals
- As a user I can read about pc builds.
- As a user I can register an account so that post content, comment and give feedback.
- As a user I can create a post so that I can show off my build for other users to enjoy.
- As a user I can use any device I want and the design will respond accordingly so that I am not bound to use only one device/browser.
- As a user I can naviagte through the main topics so that I can jump to whichever topic I want from one menu bar.


#### Returning User Goals
- As a user I can rate the post and it's content so that how I thought about the build is represented.
- As a user I can modify or delete my comment on a post so that I can correct my opinion or delete my input from the post.
- As a user I can modify or delete my posts so that I can correct my content or delete it.
- As a user I can comment on a post so that I can give my opinion on the post.
- As a user I can see comments on a post so that can read what other people have to say about the post.


#### Frequent User Goals
- As a user I can create tags on my posts and comments so that it can be searched by them.
- As a user I can search through the posts so that can find what I want to.
- As a user I can view all tags so that I can browse through them.
- As a user I can indicate the status of my input so that I knows if those things will be implemented one day or not.
- As a user I can give input/feedback so that in the future there will be new features on the website.
> additionaly the returning user goals apply here as well

## WIREFRAMES
Wireframes were produced using Balsamiq. 

 <details>

 <summary>Desktop Wireframes</summary>
Index Page:
<img src="documentation/wireframes/Index - Desktop.png" alt="Desktop Index Wireframe">

Show Build Post Page:
<img src="documentation/wireframes/Post - Desktop.png" alt="Desktop Show Build Post Wireframe">

Add/Edit Build Post Page:
<img src="documentation/wireframes/Add_Edit Post - Desktop.png" alt="Desktop Add/Edit Build Post Wireframe">

Delete Build Post Page:
<img src="documentation/wireframes/Delete Post - Desktop.png" alt="Desktop Delete Build Post Wireframe">

Search build via tags Page:
<img src="documentation/wireframes/search - desktop.png" alt="Desktop Search build via tags Wireframe">

Future Content Page:
<img src="documentation/wireframes/Future Content - Desktop.png" alt="Desktop Future Content Wireframe">

Sign-Up Page:
<img src="documentation/wireframes/Sign-Up - Desktop.png" alt="Desktop Sign-Up Wireframe">

Login Page:
<img src="documentation/wireframes/Login - Desktop.png" alt="Desktop Login Wireframe">

Logout Page:
<img src="documentation/wireframes/Logout - Desktop.png" alt="Desktop Logout Wireframe">

404 Page:
<img src="documentation/wireframes/404 - Desktop.png" alt="Desktop 404 Wireframe">

 </details>

 <details>
    <summary>Mobile Wireframes</summary>
Index Page:

<img src="documentation/wireframes/Index - Mobile.png" alt="Mobile Index Wireframe" width="50%" >

Show Build Post Page:

<img src="documentation/wireframes/Post - Mobile.png" alt="Mobile Show Build Post Wireframe" width="50%" >

Add/Edit Build Post Page:

<img src="documentation/wireframes/Add_Edit Post - Mobile.png" alt="Mobile Add/Edit Build Post Wireframe" width="50%" >

Delete Build Post Page:

<img src="documentation/wireframes/Delete Post - Mobile.png" alt="Mobile Delete Build Post Wireframe" width="50%" >

Search build via tags Page:

<img src="documentation/wireframes/search - mobile.png" alt="Mobile Search build via tags Wireframe" width="50%" >

Future Content Page:

<img src="documentation/wireframes/Future Content - Mobile.png" alt="Mobile Future Content Wireframe" width="50%" >

Sign-Up Page:

<img src="documentation/wireframes/Sign-Up - Mobile.png" alt="Mobile Sign-Up Wireframe" width="50%" >

Login Page:

<img src="documentation/wireframes/Login - mobile.png" alt="Mobile Login Wireframe" width="50%" >

Logout Page:

<img src="documentation/wireframes/Logout - Mobile.png" alt="Mobile Logout Wireframe" width="50%" >

404 Page:

<img src="documentation/wireframes/404- Mobile.png" alt="Mobile 404 Wireframe" width="50%" >

</details>



## AGILE
The agile metholody way applied for this project. The To-Do's were split according to their uer stories into sprints. To graphically represent this and not just have each sprint with its goals, tests etc on paper Github's project board was used to show this each springt and tasks as well. As I also use the agile system in my professional life (project management) I didn't always update the digital board and move user stories as I did it in my notes, hence you can see in the documentation of the board that a lot of stories were done at once. However, through my commits one can see that after each small step that worked, and through a lot of testing and fixing the code in between, one can see how this framework was well implemented into each step/sprint of the project.

>[Project Board](https://github.com/users/Xakkusu/projects/5)

My mentor adviced me to only keep sprints that are within the scope of my project. So I also implemented a section called "for next run" where future sprints are in that are possible future features but are not needed in the current project.


##  ENTITY RELATIONSHIP DIAGRAM - ERD
The following diagram illustrates the models used in this project and their relationships to one another:

<img src="documentation/pp4-erd.png" alt="ERD" >

The user model is created by [Django AllAuth](https://docs.allauth.org/en/latest/) library for user authentication, hence it was not written by me but solely installed and used. The taggit_tag was created by the [django-taggit](https://django-taggit.readthedocs.io/en/latest/) application and used for its well developed tagging system.


## FINAL DESIGN
### Imagery


### Color Scheme


The color palette was created by using the [coolors](https://coolors.co/) website.

### Typography



### Final Look
<details>
<summary>Desktop</summary>

Index Page:

<img src="x" width="90%" alt="Desktop Index Page">

 Page:

<img src="x" width="90%" alt="Desktop Index Page">


404 Page:

<img src="x" width="90%" alt="Desktop Index Page">

</details>

<details>
<summary>Mobile</summary>

Index Page:

<img src="x" width="50%" alt="Mobile Index Page">


 Page:

<img src="x" width="50%" alt="Mobile Index Page">


404 Page:

<img src="x" width="50%" alt="Mobile Index Page">

</details>

## FEATURES


All pages have the following in common:
#### Navbar
<img src="x" width="50%" alt="x">

#### Footer
<img src="x" width="50%" alt="x">



### Index Page
![Index Content](x)

...


### 404 Page
![404 Page](x)


### Future Content Page


## TESTING
### Accessibility
#### Lighthouse Testing
The main problem with my Best Practice score is that cloudinary uses http:// insteast of https:/ when transfering images.
Moreover as the user can upload images whichever format and they are made to fit the cards, the performance suffers through this, especially in mobile view as a third-party cloud-based platform can create succh problems.


##### Desktop
Index Page:

<img src="documentation/lighthouse/desktop-lighthouse-index.png" width="60%" alt="Lighthouse desktop index rating">


Show Build Post Page:

<img src="documentation/lighthouse/desktop-lighthouse-show-build-post.png" width="60%" alt="Lighthouse desktop show build post rating">


Create Build Post Page:

<img src="documentation/lighthouse/desktop-lighthouse-create-build-post.png" width="60%" alt="Lighthouse desktop create build post rating">


Edit Build Post Page:

<img src="documentation/lighthouse/desktop-lighthouse-edit-build-post.png" width="60%" alt="Lighthouse desktop edit build post rating">


Delete Build Post Page:

<img src="documentation/lighthouse/desktop-lighthouse-delete-build-post.png" width="60%" alt="Lighthouse desktop delete build post rating">


Search Build via Tags Page:

<img src="documentation/lighthouse/desktop-lighthouse-search-via-tags.png" width="60%" alt="Lighthouse desktop search via build tags rating">


Future Content Page:

<img src="documentation/lighthouse/desktop-lighthouse-future-content.png" width="60%" alt="Lighthouse desktop future content rating">


Sign-Up Page:

<img src="documentation/lighthouse/desktop-lighthouse-sign-up.png" width="60%" alt="Lighthouse desktop sign up rating">


Sign-In Page:

<img src="documentation/lighthouse/desktop-lighthouse-login.png" width="60%" alt="Lighthouse desktop login rating">


Logout Page:

<img src="documentation/lighthouse/desktop-lighthouse-logout.png" width="60%" alt="Lighthouse desktop logout rating">


404 Page:

<img src="documentation/lighthouse//desktop-lighthouse-404.png" width="60%" alt="Lighthouse desktop 404 rating">



##### Mobile
Index Page:

<img src="documentation/lighthouse/mobile-lighthouse-index.png" width="60%" alt="Lighthouse mobile index rating">


Show Build Post Page:

<img src="documentation/lighthouse/mobile-lighthouse-show-build-post.png" width="60%" alt="Lighthouse mobile show build post rating">


Create Build Post Page:

<img src="documentation/lighthouse/mobile-lighthouse-create-build-post.png" width="60%" alt="Lighthouse mobile create build post rating">


Edit Build Post Page:

<img src="documentation/lighthouse/mobile-lighthouse-edit-build-post.png" width="60%" alt="Lighthouse mobile edit build post rating">


Delete Build Post Page:

<img src="documentation/lighthouse/mobile-lighthouse-delete-build-post.png" width="60%" alt="Lighthouse mobile delete build post rating">


Search Build via Tags Page:

<img src="documentation/lighthouse/mobile-lighthouse-search-via-tags.png" width="60%" alt="Lighthouse mobile search via build tags rating">


Future Content Page:

<img src="documentation/lighthouse/mobile-lighthouse-future-content.png" width="60%" alt="Lighthouse mobile future content rating">


Sign-Up Page:

<img src="documentation/lighthouse/mobile-lighthouse-sign-up.png" width="60%" alt="Lighthouse mobile sign up rating">


Sign-In Page:

<img src="documentation/lighthouse/mobile-lighthouse-login.png" width="60%" alt="Lighthouse mobile login rating">


Logout Page:

<img src="documentation/lighthouse/mobile-lighthouse-logout.png" width="60%" alt="Lighthouse mobile logout rating">


404 Page:

<img src="documentation/lighthouse//mobile-lighthouse-404.png" width="60%" alt="Lighthouse mobile 404 rating">


#### Wave Testing
As Wave did not let me sign-in to test pages that only appear as a logged in user, only the pages that are shown without being logged in were tested.
There are some contrast-errors, but as neither lighthouse nor personal testers with minor vision disabilities had problems with them I decided to keep the contrast as it is.

Index Page:

<img src="documentation/wave/index-wave.png" alt="Wave index rating" width="40%">


Show Build Post Page:

<img src="documentation/wave/show-build-post-wave.png" alt="Wave show build post rating" width="40%">


Create Build Post Page:

<img src="documentation/wave/create-build-post-wave.png" alt="Wave create build post rating" width="40%">


Search Build via Tags Page:

<img src="documentation/wave/search-via-tags-wave.png" alt="Wave search build via tags rating" width="40%">


Future Content Page:

<img src="documentation/wave/future-content-wave.png" alt="Wave future content rating" width="40%">


Sign-Up Page:

<img src="documentation/wave/register-wave.png" alt="Wave sign-up rating" width="40%">


Sign-In Page:

<img src="documentation/wave/login-wave.png" alt="Wave login rating" width="40%">


404 Page:

<img src="documentation/wave/404-wave.png" alt="Wave 404 rating" width="40%">


### W3C Validators
#### HTML
There were some errors shown in the W3C Markup Validator which I was able to fix like errors with the alpine.js. Here are all the W3C results with minor warnings and tips, which will be looked at when time resource free themselves:

<details>
<summary>No Errors</summary>

Index Page

<img src="documentation/validators/html-val-index.png" alt="W3C HTML validator index" width=60%>


Create Build Post Page

<img src="documentation/validators/html-val-create.png" alt="W3C HTML validator create build post" width=60%>


Edit Build Post Page

<img src="documentation/validators/html-val-index.png" alt="W3C HTML validator edit build post" width=60%>


Delete Build Post Page

<img src="documentation/validators/html-val-delete.png" alt="W3C HTML validator delete build post" width=60%>


Search via tags Page

<img src="documentation/validators/html-val-search.png" alt="W3C HTML validator search via tags" width=60%>


Future Content Page

<img src="documentation/validators/html-val-future.png" alt="W3C HTML validator future content" width=60%>


Sign-In Page

<img src="documentation/validators/html-val-sign-in.png" alt="W3C HTML validator sign-in" width=60%>


Logout Page

<img src="documentation/validators//html-val-logout.png" alt="W3C HTML validator logout" width=60%>


Sign-Up Page

<img src="documentation/validators/html-val-sign-up.png" alt="W3C HTML validator Sign-up" width=60%>

</details>


#### CSS
No errors were returned for the CSS stylesheet from the W3C CSS Validator:

<img src="documentation/validators/html-val-CSS.png" alt="W3C CSS validator" width=60%>


### JShint
[JSHint](https://jshint.com/) was used to validate the JavaScript.
<details>
<summary>comments.js</summary>
No errors or warnings.

<img src="documentation/js/JSHint-testing.png" alt="comments.js JSHint result">
</details>

<details>
<summary>datepiker.js</summary>
No errors or warnings.

<img src="documentation/js/JSHint-testing-datepicker.png" alt="datepiker.js JSHint result">
</details>


### PEP8 
No errors were returned for all python files from the [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) testing:
<details>
<summary>build_your_dream</summary>
No errors or warnings for all python files in build_your_dream.

urls.py:

<img src="documentation/python/pep8-urls.png" alt="urls.py PEP8 result">


settings.py:

<img src="documentation/python//pep8-settings.png" alt="settings.py PEP8 result">



</details>
<details>
<summary>builds</summary>
No errors or warnings for all python files in builds.

urls.py:

<img src="documentation/python/pep8-build-urls.png" alt="urls.py PEP8 result">


admin.py:

<img src="documentation/python/pep8-build-admin.png" alt="admin.py PEP8 result">


forms.py:

<img src="documentation/python/pep8-build-forms.png" alt="forms.py PEP8 result">


models.py:

<img src="documentation/python/pep8-build-models.png" alt="models.py PEP8 result">


views.py:

<img src="documentation/python/pep8-build-views.png" alt="views.py PEP8 result">


serializers.py:

<img src="documentation/python/pep8-build-serializers.png" alt="serializers.py PEP8 result">



</details>
<details>
<summary>future_content</summary>
No errors or warnings for all python files in future_content.

urls.py:

<img src="documentation/python/pep8-future-url.png" alt="urls.py PEP8 result">


admin.py:

<img src="documentation/python/pep8-future-admin.png" alt="admin.py PEP8 result">


forms.py:

<img src="documentation/python/pep8-future-forms.png" alt="forms.py PEP8 result">


models.py:

<img src="documentation/python/pep8-future-model.png" alt="models.py PEP8 result">


views.py:

<img src="documentation/python/pep8-future-view.png" alt="views.py PEP8 result">



</details>

### Form Testing

### Links Testing
- All internal links are working and redirecting the user to the pages they are meant to redirect them to. 
- All external links are working and redirecting, through a separate tab, the user to the external website they are meant to be redirected to.


### Browser Testing
The website was successfully tested on the following browsers:
- Google Chrome
- Mozilla Firefox
- Safari
- Microsoft Edge

### Device Testing
- This website was viewed and tested on various devices such as smartphones (Iphone X, Samsung Galaxy S20, Iphone 13, Huawei P40 Pro+), laptops and desktops to guarantee that it is responsive for several screen sizes. Full successful testing was performed on all of the devices.


- The following websites, besides google dev tools, were used to check responsiveness:
    - [Am I Responsive - Index Page](https://ui.dev/amiresponsive?url=https://xakkusu.github.io/)
    - [Am I Responsive -  Page](x)
    - [Am I Responsive - 404 Page](hx)
    - [Responsinator - Index Page](x)
    - [Responsinator - Page](x)
    - [Responsinator - 404 Page](x)

### User Stories Testing
#### First Time User Goals


#### Returning User Goals

#### Frequent User Goals


### Fixed Bugs
1. 

2.  


3. 

### Known Bugs


## TECHNOLOGIES USED
### Languages
- HTML
- CSS
- JavaScript

### Frameworks, Libraries and Programs used
- [Balsamiq](https://balsamiq.com/wireframes/)- Used to create wireframes.
- [GitHub](https://GitHub.com/) - Used for version control and hosting.
- [Gitpod](https://gitpod.io/) - IDE to develop the website.
- [Google Fonts](https://fonts.google.com/) - Used to import  fonts used on the website.
- [Google Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools)- Used for troubleshooting, debugging, inspecting page's elements, testing responsiveness and styling elements.
- [Coolors](https://coolors.co/) - Used to create a color palette.
- [Google Chrome's Lighthouse](https://developers.google.com/web/tools/lighthouse) - Used to test performance and accessibility.
- [W3C HTML Markup Validator](https://validator.w3.org/) Used to validate HTML code.
- [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) Used to validate CSS code.
- [JSHint](https://jshint.com/) Used to test all Javascript code.
- [Am I Responsive](https://ui.dev/amiresponsive) Used to test responsiveness.
- [Responsinator](http://www.responsinator.com/) Used to verify responsiveness especially usage for mobile devices.
- Code Institute's Gitpod Template to generate IDE workspace.


## DEPLOYMENT
The steps to deploy this project using GitHub pages were the following:
1. Go to the Settings tab of your GitHub repository.
2. On the left-hand sidebar, in the Code and automation section, select "Pages".
3. Make sure to select the following:
    - Source is set to 'Deploy from Branch'.
    - Main branch is selected.
    - Folder is set to / (root).
4. Click Save next to /root.
5. "Your GitHub Pages site is currently being built from the main branch." shows up.
6. Go back to the Code tab. Wait a few minutes for the build to finish and refresh your repository where a Deployments section will show the deployed project.

The live link can be found here - [X](h)

How to run the project locally:

Fork the repository:
- Log in (or sign up) to Github.
- Go to the repository for: Xakkusu/bioshock-quiz.
- Click the Fork button in the top right corner.

#### Clone repository:
1. Log in (or sign up) to GitHub.
2. Go to the repository for: Xakkusu/bioshock-quiz.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.
6. A clone of the repository will now be created on your machine.


## CREDITS
### Media
The following images were gratefully used:
- [X Image](x) - Wallpapaerflare


### Resources
- Tutorials from Code Institute's lessons that we learned in the course of our diploma-education used to understand the basic concepts of JavaScript. 

- [Stack Overflow](https://stackoverflow.co/)

- [MDN](https://developer.mozilla.org/en-US/)

- [W3Schools](https://www.w3schools.com/)

- 


## ACKNOWLEDGEMENTS
- Code Institute for informative course material.