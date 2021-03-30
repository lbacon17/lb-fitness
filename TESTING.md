# **[LB Fitness](https://lb-fitness.herokuapp.com/)**

# Testing

This file documents the testing process of the project.

## Table of contents

* [Validation](#validation)
* [Responsiveness](#responsiveness)
* [Browser Compatibility](#browser-compatibility)
* [Testing User stories](#testing-user-stories)
* [Issues and bugs](#issues-and-bugs)

### Validation

#### Python

#### JavaScript

#### CSS

### HTML

[Back to TOC](#table-of-contents)

### Responsiveness

The website was tested in Google Chrome using the Viewport Resizer extension, Chrome DevTools and the Responsive Design Checker.

The website's layout was tested pixel by pixel and on all popular mobile and tablet devices. The design is consistently responsive at all screen sizes and there is no change in the appearance or performance of interactive features.

No issues, major or minor, were found.

[Back to TOC](#table-of-contents)

### Browser Compatibility

The application was tested in the following browsers:

* Google Chrome
* Mozilla Firefox
* Brave Browser
* Opera
* Safari

The application proved itself highly compatible with all browsers and performance was consistent across the board. Only one minor issue was noted:

Smooth scroll behaviour is not supported on Safari, meaning the page jumps right back to the top when the return to top button is clicked as opposed to a smooth scrolling motion. This is due to Safari not supporting the scroll-behavior: smooth CSS property.
I tried various JavaScript solutions to remedy this, but none of them had any effect, and some even hindered the app's performance. As this is a relatively minor issue, I decided not to take any further action at this stage.

[Back to TOC](#table-of-contents)

### Testing User stories

**Registration, accounts and subscription**

* As a first-time visitor, I want to immediately understand app's main purpose
    * As soon as I land on the homepage I can see the app provides training advice and merchandise, and the big call-to-action button lets me know its main offering is a subscription service
* As a user, I want to create a free account for a fitness app
    * The green button on the homepage tells me that having an account is free of charge, and I can also see the Register button in the navbar
    * I click on one of these buttons, enter a username, e-mail address and password and click Sign Up
    * An e-mail immediately arrives in my inbox with a link to confirm my e-mail address, so I click on the link and confirm
    * I'm now able to log into my account using my login details
* As a user, I want to try out a subscription to a fitness app to see if it’s right for me
    * On the homepage banner underneath the navbar, I can see that all subscriptions offer a two-week free trial
    * I click the subscribe button and read the features of each plan to decide which one is right for me
    * After I've chosen a plan, I click on it, enter my customer and payment details and check out securely
* As a user, I want to subscribe in order to access content that will help get me in shape and make me feel healthier
    * 
* As a member, I want to be able to access material only available to paid subscribers.
* As a member, I want to comment on and give feedback on the material available to me, and potentially interact with other members in this space.
* As a member, I want to edit and delete my comments.
* As a member on the most expensive plan, I want to be able to buy items from the store at a discounted price as a reward for my loyalty.
* As a user, I want to be able to log in and out of my account
* As a user, I want to be able to update my account details such as my username, email address and password
* As a user, I want to be able to view my order history and save my delivery and payment details
* As a member, I want to be able to cancel my subscription
* As a user, I’ve decided this app isn’t for me and want to delete my account

**Purchasing and checkout**

* As a user, I want to purchase fitness-related products such as training gear and prepared healthy meals that reflect my lifestyle
* As a user, I want to be able to select and adjust the quantity or size of a product that I’m about to purchase
* As a user, I want to view the items in my shopping cart
* As a user, I want to be able to see real-time updates of the value of my shopping cart and a preview of its items without having to visit the cart page
* As a user, I want to be able to make a purchase from the store using my credit card and easily enter my payment details
* As a user, I want to be able to save my information when making a purchase, so I don’t have to fill out the form again on my next purchase
* As a user, I want to feel confident that my personal and payment information is safe and secure 
* As a user, I want to see confirmation of my order after completing a purchase.
* As a user, I want to receive a confirmation e-mail after making a purchase.

**Searching, reading and sorting**

* As a user, I want to be able to search for products in the store using keywords so that I can potentially purchase some
* As a member, I want to be able to search for material that I have access to so that I can easily find what I'm looking for
* As a user or member, I want to be able to see my search results
* As a user or member, I want to be able to see the number of results
* As a user, I want to be able to sort products according to different criteria such as name and price, so that I can find what I want easier or see what has the most recommendations
* As a member, I want to be able to sort videos according to different criteria such as length and rating
* As a user, I want to be able to read about a product’s individual details
* As a user, I want to contact the site owner with a question and recieve a confirmation e-mail that my query has been received
* As a user of the app, I want to read about its owner and find out more about the business

**Administrator**

* As an administrator, I want to add a product to the store
* As an administrator, I want to edit a product’s specifications or update its details
* As an administrator, I want to delete a product from the store
* As an administrator, I want to add a video to the site that is accessible to members
* As an administrator, I want to edit a video's details such as replacing its actual file, updating its title or description or fixing an incorrect value for its duration
* As an administrator, I want to categorise videos so that some are only accessible to premium members
* As an administrator, I want to delete a video from the database
* As an administrator, I want to be able to approve or reject comments on videos by users so that all content on the site remains appropriate and makes for an enjoyable experience for all members

[Back to TOC](#table-of-contents)

### Issues and Bugs

[Back to TOC](#table-of-contents)

[Back to README](README.md)