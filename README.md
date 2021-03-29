# **[LB Fitness](https://lb-fitness.herokuapp.com/)**

Welcome to LB Fitness. This application is a place for users to educate themselves about the basics of fitness...

This application was inspired by one of the [Code Institute](https://codeinstitute.net/)'s project ideas: **build a fitness subscription application**.

The deployed website is available [here](https://lb-fitness.herokuapp.com/).

## Table of contents

* [UX](#ux)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Data Structure](#data-structure)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits and Acknowledgements](#credits-and-acknowledgements)

### UX

#### Design

The website is mainly based on Bootstrap's grid layout, and makes use of a number of Bootstrap's components and built-in classes, such as the navbar, buttons and spacing rules. The design mixes vibrant and muted colours in order to stand out to the user but remain easy on the eye and make the website as intuitive and easy to navigate as possible. To new and unauthenticated users, the site's primary purpose as a subscription application is immediately obvious with the background image, the chunky, shadowed callout text and the large call-to-action button inviting the user to subscribe. The choice of font 'RocknRoll One' gives the site a fun feel without appearing comical.

Datasets consist of one item per row on extra small screens, one or two items per row on small screens, 2 or 3 items per row on medium screens, 3 items per row on large screens, and 3 or 4 items per row on extra large screens. Any page or app with potentially varying amounts of data is fully responsive at all screen sizes and the site's structural integrity is not harmed. Data pertaining to user history or key information is formatted in a table to make information easily accessible to the user.

User feedback is clear, with messages appearing in a card at the top left of the screen (top centre on mobile devices with reduced font-sizes for optimal user-friendliness). The user is immediately notified of the nature of the message by the background colour of the card title - a green colour indicates a success message i.e. the user has successfully performed and completed an action, a red colour indicates an error message, yellow indicates a warning to the user and blue simply indicates some information that the user may wish to be aware of. All messages are dismissible with a click of the 'x' in the top-right corner of the card, so that the user does not have to keep reading the message once it has been acknowledged.

All delete actions initiated by the user that will result in data being permanently deleted trigger a modal pop-up box, asking the user to confirm that they really want to delete something in the event that they mistakenly clicked that button. The user can select cancel, marked with a more neutral grey background, if they do not wish to delete a piece of data, or confirm, which will initiate the deletion process. Note that this does not apply to a user removing an item from their shopping cart, as the item will still be retrievable in the store and the user can re-add it if they wish. Asking the user to confirm every individual action may frustrate them and unnecessarily slow down their navigation of the app. All buttons that perform a delete action have a red background.

Forms on the website utilise the django-crispy-forms package for maximum responsiveness. Those that also require card payment use Stripe Elements for authorisation and payment processing.

#### User Stories

**Registration, accounts and subscription**

* As a user, I want to subscribe in order to access content that will help get me in shape and make me feel healthier
* As a user, I want to try out a subscription to a fitness app to see if it’s right for me
* As a user, I want to create a free account for a fitness app
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

#### Wireframes

### Features

#### Existing features

* A responsive fixed navbar displaying with the ability to navigate to all the site's main pages, register for an account, log in/out and view the total value of the user's shopping cart
* 


##### For all users

##### For registered users

##### For members (paid subscribers)

##### For administrators (superusers)

#### Feature left to implement

[Back to TOC](#table-of-contents)

### Technologies Used

Django
Django-Allauth (for user authentication)

[Back to TOC](#table-of-contents)

### Data Structure

[Back to TOC](#table-of-contents)

### Testing

[Back to TOC](#table-of-contents)

### Deployment

To install Django `pip3 install django`

To create project in current directory `django-admin startproject lb-fitness .`


[Back to TOC](#table-of-contents)

### Credits and Acknowledgements

[Back to TOC](#table-of-contents)
