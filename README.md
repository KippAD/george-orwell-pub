# The George Orwell Pub

<img  src="static/images/home.png" alt="Wireframes of the project" width="45%">
<img  src="static/images/events.png" alt="Wireframes of the project" width="45%">

The George Orwell Pub website is a django based project for a fictional business developed for my fourth milestone project at Code Institute.

## Brief

The George Orwell Pub website serves as a point of information and booking system for a pub and restaurant based in Montpellier, France. Customers will be able to create an account, view upcoming events, and make bookings. Within their account they will be able to manage these bookings, as well as contact the site Admin with any queries that they might have. 

The objective of the project is to create an aesthetically pleasing design with functionality that allows users to access and interact with content easily, and that allows an Admin to intuitively control the data that the site works with.. 

## UX

Users of the George Orwell Pub website would most likely be young adults in and around the area - many of which might be regulars that would be revisiting the site to book an event on a weekly basis. This means that navigating through the booking system should be as fast and easy as possible, so that users who only need to make a booking can do so without hassle.

###  User Stories

**Epic: Site Management**
- As an **admin** I can **login to an admin panel** so that I can manage my website
- As an **admin** I can **create events** so that I can notify site visitors of the business schedule
- As an **admin** I can **update existing events** so that **I can keep the schedule up to date**
- As an **admin** I can **delete events** so that **I can cancel events that are no longer going to happen**.
- As an **admin** I can **delete bookings** so that I can cancel existing bookings if necessary
- As an **admin** I can **delete users** so that **I can remove existing users if necessary**
- As an **admin** I can **view and respond to user queries** so that **I can interact with my clientele**

**Epic: Event Booking**
- As a **user** I can **register an account** so that I can book my place at events and send site queries.
- As a **user** I can **sign in and out of my account** so that **access to my account and data is limited**
- As a **user** I can **book events** so that I can reserve a place at events of my choosing
- As a **user** I can **update my existing bookings** so that I can add or remove people on my reservation
- As a **user** I can **delete an existing booking** so that I can remove my reservation if I no longer wish to come

**Epic: Account Management**
- As a **user** I can **request an account deletion** so that I can remove my account from the site**
- As a **user** I can **send a query to the admin** so that **I can contact them with any questions of request I have**

## Agile Development

Using the User Stories above the site was developed using AGILE methodology. Components and features in the website were designed in order to meet the criteria of the user stories and each stage of development revolved around resolving each user story incrementally. 

<img  src="static/images/project-board.png" alt="Agile project board" width="100%">

This meant that each component added to the site could be prioritized by the importance of its corresponding user story.

## Design

### Design Objective
- The site is attractive and first time users want to return to it.
- Site actions are intuitive so that a user knows how to interact with content.
- The site is functional and errors and the user will be appropriately redirected when faced with errors
- Content is meaningfully organized by its priority

### Wireframes
The wireframes for the George Orwell Pub were made with Figma. Designs for multiple viewport sizes were created in order to create a design that would be responsive on various devices.

<img  src="static/images/wireframes.png" alt="Wireframes of the project" width="100%">

The final design holds true to the original concepts, but as development progressed certain aspects differed. This was usually due to design preference changing as time went on, and certain components looking better in the browser than they did in the wireframe.

### Color Scheme/Typography

The Color Scheme of the website was generated using [**Coolors**](https://coolors.co/). Outside of the home page most of the colors are black and white - this simple scheme was chosen to represent pen and paper as the business is named after the writer George Orwell. 

The fonts on the site are Montserrat, Chivo, Istok Web, and Heebo.

## Features

### Existing

<img  src="static/images/home-page-1.png" alt="Home page" width="34%">
<img  src="static/images/home-page-2.png" alt="About us section" width="30%">

**Homepage:** The homepage is the first area that the user sees when entering the website. It includes a summary of the business and what it does, as well as clear navigation to other areas of the site and a carousel of upcoming events.

---

<img  src="static/images/events.png" alt="About us section" width="50%">

**Events Page:** The events page displays all upcoming events with the relevant information about them (Date, capacity, price). Each event is a collapsible element, revealing the event description when clicked on - this keeps the content more concise and allows the user to unravel information as they choose to. The user can also book an event by clicking on the Book now button and filling out the form. If an admin is logged in they are able to access full CRUD functionality for each event, as well as creating new events.

---

<img  src="static/images/event-card.png" alt="Booking event card" width="30%">
<img  src="static/images/booking-form.png" alt="Booking form" width="30%">
<img  src="static/images/booking-account.png" alt="Account page" width="30%">

**Booking System:** The booking system allows users to reserve places for events of their choosing. There is full form validation preventing users from making double bookings and also from events becoming overbooked. 

---

<img  src="static/images/contact-form.png" alt="Contact form" width="25%">
<img  src="static/images/contact-success.png" alt="Contact success" width="30%">
<img  src="static/images/contact-email.png" alt="Contact email" width="20%">

**Contact Form:** The contact form allows users to send queries to the admin. This form is linked to Amazon Web Services SES, meaning that the user’s messgae will appear in the gmail account of the site.

---

<img  src="static/images/account-1.png" alt="Account bookings tab" width="45%">
<img  src="static/images/account-2.png" alt="Account info tab" width="45%">

**Account Page:** The account page allows users to view, update, and delete their existing bookings. It will also display their account information in a separate tab.

---

<img  src="static/images/admin-events.png" alt="Admin events panel" width="30%">
<img  src="static/images/admin-bookings.png" alt="Admin bookings panels" width="30%">
<img  src="static/images/admin-user.png" alt="Admin user panel" width="30%">

**Admin Interface:** The admin interface displays all events, bookings, and users where the admin can perform CRUD functionality on each of their models.

-- 

<img  src="static/images/admin-events.png" alt="Admin events panel" width="30%">
<img  src="static/images/admin-bookings.png" alt="Admin bookings panels" width="30%">

**User Feedback Pages:** Unsuccessful bookings will redirect the user to a page explaining why their submission was rejected. Similarly a successful booking and contact form submission will display a success page.

--

<img  src="static/images/admin-events.png" alt="Sign up form" width="80%">

**Accounts:** Users can register an account and login/logout. Once authenticated they are able to interact with the sites content.

---

## Future
Here are some future features that were outside of the project scope on the current iteration of development but could be included to improve the user experience and site in general.

- **Form Submission Email:** User receives an email when an account is created or when a booking is made.
- **Waiting List:** Users will have the option to join a waiting list for full events and receive an email if there is availability.
- **Prefilled Booking Form:** Booking form is prefilled with the event and can be replaced with a select form if the user chooses.
- **Repeating/Self Deleting Event:** Events can be set to repeating so that they automatically appear on the schedule each week, and events in the past self-delete.

- **Messaging In Browser:** User and admin can message within the website from the account and admin panels respectively.
- **Menu:** Admin has access to CRUD functionality for a menu.
- **Admin Interface for User:** Whilst the admin can see users in the admin panel, it redirects the admin to the default django admin dashboard, so CRUD functionality for the user within the website would provide a better experience for the site owner.

## Testing 

### **Python**
All of the site forms are validated, with automated testing to ensure that correct inputs are given. CRUD functionality on the both booking and events have been manually tested in the deployed site - and all actions affecting the database work as expected. PEP8 warnings from the IDE have all been resolved in the custom code. The contact form functionality has been tested to ensure that it works.

---

<img  src="static/images/html-warnings.png" alt="W3C HTML" width="80%">

### **HTML**
There were various HTML errors that arose in the W3C HTML validator ranging from mispelled href attributes to unclosed elements. The validator shows many errors relating to jinja that are intentionally unresolved, but all other warnings were fixed.

---

<img  src="static/images/css-validator.png" alt="W3C HTML" width="80%">

### **CSS**
The CSS validator returned a small amount of errors that were mainly typos. Now the validator returns no warnings or errors.

---

### **Responsiveness**
The website is responsive and has been tested accross all viewport sizes of a greater screen width of 320px. The specific devices are the included templates of Chrome Developer Tools:

<img  src="static/images/devices.png" alt="W3C HTML" width="20%">

**Notes**:

- Event buttons are centered on Ipad Mini
- Ipad Mini causes some other spacing issues
- Tests exclude Galaxy Fold (Viewport width of 280px)

Testing the responsiveness included checking that every link worked and every component behaved as expected, as well as ensuring that the app design was maintained on smaller devices. Throughout the process all bugs found were resolved, and now all responsiveness is retained accross the tested devices and all actions work as expected.

--

**Browser Testing**
The website has been tested on the following browsers:

- **Chrome**

- **Mozilla Firefox**

- **Safari**

- **Opera**

The testing process involved manually checking the responsiveness of every sit page on each browser, as well as ensuring that every link and button worked correctly. Similarly each action that worked with the backend was checked against he database to confirm that the application works as expected accross all of the browsers.

--

**Lighthouse Testing**

Chrome Developer Tools Lighthouse testing rates the performance, accessibility, best practices and SEO of a website.

**Home Page**

<img  src="static/images/home-lighthouse-1.png" alt="Lighthouse testing home desktop" width="40%">
<img  src="static/images/home-lighthouse-2.png" alt="Lighthouse testing home mobile" width="40%">

**Events Page**

<img  src="static/images/events-lighthouse-1.png" alt="Lighthouse testing events desktop" width="40%">
<img  src="static/images/events-lighthouse-2.png" alt="Lighthouse testing events mobile" width="40%">

**Account Page**


## **Bugs**

### Resolved

- **Booking Capacity** - A persistent bug was that a new booking would be rejected if it was within 2 of the capacity. This meant that there were always two spaces free in an events that could not be taken up. It was eventually resolved with the correct query.

- **Leaked SMTP** - When creating the automatic contact form, the email app password and username were accidentally included in a commit. The email was flooded with scam messages and dodgy emails, so was replaced with a new email to resolve the issue.

### Unresolved

- **User Booking Update** - Users can access another user's booking by the URL - this bug was unfortunately found too late in deployment to resolve before the project was due to be submitted.

- **User Reset Password** - Users cannot request an email to reset their password because AWS Simple Email Service requires that every recipient be activated via an email link. This can be resolved by applying to move out of sandbox mode in AWS - if accepted, the code to redirect password resets to email is included in the contact form.


## **Technologies**
The George Orwell Pub was built with the following technologies:

1.  [**Django**](https://www.djangoproject.com/) - Web framework used to develop application.
2.  [**Bootstrap**](https://getbootstrap.com/) - Front end library used to build the site UI.
2.  [**Python**](https://www.python.org/) - Used for the backend.
3.  [**HTML**](https://en.wikipedia.org/wiki/HTML5) - Content and semantic meaning.
4.  [**CSS**](https://en.wikipedia.org/wiki/CSS) - Custom styling and responsiveness.
5.  [**JQuery**](https://jquery.com/) - Javascript library used for custom interactivity.
6.  [**Gitpod**](https://gitpod.io) - The IDE used for development.
7.  [**Heroku**](https://dashboard.heroku.com/apps) - Project hosting.
9.  [**Figma**](https://figma.com/) - Used for site design.
10. [**Font Awesome**](https://fontawesome.com/) - Icon library used.
13. [**Coolors**](https://coolors.co/) - Colour pallete generator.
14. [**Real Favicon Generator**](https://realfavicongenerator.net/) - For favicon creation.

## **Deployment**

### **To deploy the project**
Heroku was used to host the George Orwell Pub website:

1. Sign in to Heroku and navigate to the Heroku Dashboard.

2. Click **New** in the top right of the browser, and then **Create New App**.

3. Once created, head over to **Settings** and then **Reveal Config Vars**.

4. Withing your config vars, fill out the key and value pairs from you env.py file so that Heroku can reference their values.

5. Now you can add the necessary build packs in the **Settings** panel.

6. In the **Deploy** tab, find **Connect to Github**.

7. In the search bar look for the chosen repository and click **Connect**. You can also choose to **Enable Automatic Deploys**.

8. The deployed site can now be viewed.

## Cloning Project
This repository is hosted on GitHub and can be cloned and further developed by other developers:

1. Head to the repository and open the **Code** drop down menu.

2. Within the **clone** box, copy the https url.

3. Within your IDE run the command **git clone** followed by the https url in the terminal.

4. The IDE will then populate with the cloned repository files.

## Credits

[**Bootstrap**](https://getbootstrap.com/) - The project UI was built fundamentally with Bootstrap components with custom stylings on top.

[**Data Tables**](https://datatables.net/examples/basic_init/index.html) - The tables in the account and admin page were taken from the Data Table library.

[**ContactForm**](https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend) - The contact form and the backend code to wire it up to an email was from this tutorial on how to creat a contact form by **OrdinaryCoders**

[**Date Validation**](https://stackoverflow.com/questions/70558856/django-how-to-prevent-to-accept-future-date) - The Stack Overflow user **Willem Van Onsem** provided a solution to preventing the date field in the event form from accepting past dates which was implemented in my code.

I want to thank Precious Ijege and Rohit Sharma for their help in planning and advice in development of this project. Also to my fellow students on Slack who provided me with support ajd answers for any question or issue that I might have.


## Reflection 
This project was particularly challenging for myself coming off the back of a leave of absence and integrating technologies that I had never used before. Getting to grips with Bootstrap and Django meant that at times it was hard to develop the project that matched the agile project board. Similarly, I had to be a lot more flexible with the intended components and features because when I developed the scope of the project I did not have any reference point of working with these technologies before - this did mean sacrificing on what I actually wanted to develop in order to meet the deadline. It was a steep learning curve, but in future projects I will have a much greater understanding of how to plan and implement the required aspects to a standard that I am more content with.
