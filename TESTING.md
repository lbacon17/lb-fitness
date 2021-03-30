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
        * If I try to get a plan without being logged in, I'm redirected to the login page where I can enter my details
    * After I've chosen a plan, I click on it, enter my customer and payment details and check out securely
    * On the checkout page, it tells me that I will only be charged at the end of the two-week trial period and am able to cancel at any time if it's not for me
    * I receive a confirmation e-mail of my subscription details, and can see my subscription in the user dashboard
* As a user, I want to subscribe in order to access content that will help get me in shape and make me feel healthier
    * I choose a subscription, enter my details and receive confirmation
    * On the homepage, I can view my user dashboard or user profile and see my subscription in there, with details of what plan I'm subscribed to
    * Within the details is a link to the video content I'm able to view now I'm subscribed
* As a member, I want to be able to access material only available to paid subscribers
    * I navigate to the videos page to access the material and can read the details of each video
    * I can play each video on the page, or click on the video's title to be taken to the video's individual page where the video takes up more screen real estate
    * I also have the option of viewing each video in full screen mode
* As a member, I want to comment on and give feedback on the material available to me, and potentially interact with other members in this space.
    * I navigate to a video's page and write a comment in the comments section
    * After I click on submit, I'm notified that my comment is pending moderation and will not appear until approved by an administrator
        * This gives me more confidence that users will not be able to post spam in the comments section, as these comments will be rejected
    * Once my comment is approved, I can see it in the comments section and the number of comments has updated
* As a member, I want to edit and delete my comments.
    * I navigate to the video's page where I've left a comment, click the Edit button and enter my new message
    * After I click on submit, I'm notified that my comment must be re-approved by an administrator
        * This makes sense because otherwise users who wanted to spam the comments section could circumnavigate the rules by editing their own comments that had been approved
    * I can delete my comment by clicking on the Delete button, which triggers a pop-up asking me to confirm its deletion
        * If I accidentally clicked delete, I click Cancel and the pop-up closes
        * If I'm sure I want to delete my comment, I click Delete again and my comment has now disappeared
* As a member on the most expensive plan, I want to be able to buy items from the store at a discounted price as a reward for my loyalty.
    * I can see that one of the features of the VIP plan is a 50% discount and free delivery on all store orders
    * I subscribe to the VIP plan, navigate to my dashboard and see confirmation that I can store items at a dscount
    * I use the navbar to visit the Shop page and can see the usual price of each item is crossed out with a discounted price available
    * I add a few items to my cart and the total is half of what it would usually be
    * If I go to the checkout page, the total amount my card will be charged is 50% of the usual price and I can see delivery has remained at £0.00, even if my order is under £50
* As a user, I want to be able to log in and out of my account
    * When I land on the homepage, I click Login in the navbar, enter my details and log in
    * If I want to log out, I click the My Acccount dropdown menu in the navbar, select log out and confirm that I want to sign out
        * If I accidentally clicked this link, I have the option of the Keep me signed in button, which returns me to the homepage
* As a user, I want to be able to update my account details such as my email address and password
    * I click the My Account dropdown menu in the navbar and select My Profile
    * On my profile page, I have the option to change my password or update my details
        * To change my password, I enter my current password and a new password, click confirm and can log in with my new password
        * If I click Update Details, I can change the e-mail address I use for orders and also enter my default delivery information so I don't have to enter this each time when checking out
* As a user, I want to be able to view my order history and save my delivery and payment details
    * I navigate to my profile page and can see a table with my order history that includes my order number, the date of the order and the amount I paid
    * If I click on an individual order number, I can view further details such as the contents of the order
    * If I haven't placed any orders yet, the table tells me that I don't have any order history
* As a member, I want to be able to cancel my subscription
    * I go to my dashboard or profile page and click the Cancel Susbcription button, which triggers a pop-up box asking me to confirm
    * If I accidentally clicked Cancel, I click the Back button to safely dismiss the pop-up box
        * Note that this button is named Back rather than Cancel, because the action here is to cancel the subscription, so having two buttons with the word cancel could potentially confuse the user
    * To confirm cancellation, I click Cancel Subscription again and I am notified that my subscription has been cancelled
* As a user, I’ve decided this app isn’t for me and want to delete my account
    * I go to my profile page and click the Delete Account button, which triggers a pop-up box
    * If I accidentally clicked on this button, I can dismiss the pop-up by clicking Cancel
    * Otherwise I click Delete Account again, and am notified that my account has been deleted and am logged out of the app

**Purchasing and checkout**

* As a user, I want to purchase fitness-related products such as training gear and prepared healthy meals that reflect my lifestyle
    * I click the Shop dropdown menu in the navbar and select All Items, where I can view all products in the store and see how many exist
    * Below each product, I can click the add to cart button and confirm what quantity - and size, if the item has sizes - of the item I want to add to my cart
* As a user, I want to be able to select and adjust the quantity or size of a product that I’m about to purchase
    * In addition to the above, I can click on a product's image to be taken to the product's individual page where I can select my desired size and quantity
    * I click the add to cart button and receive a notification that the item was added to my cart, and in what size and quantity
* As a user, I want to view the items in my shopping cart
    * In the top-right corner of the screen, if I click on the dropdown menu, I can see a preview of my cart that lists the quantity and size of each item
    * If I click on one of them, I am taken to the cart page where I can view my cart in full screen mode
* As a user, I want to be able to adjust the quantity of an item in my cart on the cart page itself
    * On the cart page, I adjust the quantity of an item using the + and - buttons in the Quantity column
    * Once I've selected the desired quantity, I click the Update button and receive a notification that the quantity has been successfully updated
* As a user, I want to be able to remove an item from my cart
    * On the cart page, I click the x button in the row of the item I want to remove, and receive a notification that the item has been removed from my cart
* As a user, I want to be able to see real-time updates of the value of my shopping cart and a preview of its items without having to visit the cart page
    * I can see the cart total in the top right of my screen
    * Each time I add an item to the cart, the total automatically updates, adding on the price of the item that I selected
* As a user, I want to be able to make a purchase from the store using my credit card and easily enter my payment details
    * From the Cart page, I navigate to the Checkout page where I'm informed how much my card will be charged
    * I enter my delivery and payment information and enter my payment details before checking out
* As a user, I want to be able to save my information when making a purchase, so I don’t have to fill out the form again on my next purchase
    * When filling out the form on the Checkout page, I click the checkbox at the bottom of the order form to save my delivery information to my profile
    * After the order has gone through, I navigate to my profile page, click on Update Details and can see that the form is pre-filled with the data I entered on the order form
* As a user, I want to feel confident that my personal and payment information is safe and secure 
    * If I enter incorrect payment details when checking out, the app will return an error informing me that my card details are invalid and prevent the order from processing
    * If I check out again, I have to re-enter my card details so that I know they have not been stored anywhere 
* As a user, I want to see confirmation of my order after completing a purchase.
    * After I my order has been processed, I am redirected to an order confirmation page where I can see the details of my order
    * This page does does not automatically redirect after a given time so I can stay on it as long as I like and take my time reading about my order, with a button to take me back to the homepage once I'm done
    * Even once I've left this page, I can go to my profile page and locate the order in my order history
        * As the orders are ordered by date, starting with the newest, my order should be at the top of the table
        * If I click on the order number, I can view the details of the order again 
* As a user, I want to receive a confirmation e-mail after making a purchase.
    * After successfully checking out, I receive an automated e-mail confirming my order that contains the contents of my order and delivery information
    * The e-mail is sent to the e-mail address I entered when checking out, so I will receive this e-mail if this is a valid e-mail address that belongs to me

**Searching, reading and sorting**

* As a user, I want to be able to search for products in the store using keywords so that I can potentially purchase some
    * I enter a search term in the search field within the navbar and am redirected to the shop page that displays all the results containing my search parameter along with the number of items found
    * If my search query returned no items, I can click a button to view all the shop's products so I don't have to come off the shop page or scroll back to the top of the screen to enter another query
* As a user, I want to be able to filter products in the store according to category
    * In the Shop dropdown menu, I navigate to the cateogry I want to browse and click on it
    * The page now only displays items in the selected category, and tells me how many currently exist
* As a member, I want to be able to search for material that I have access to so that I can easily find what I'm looking for
    * I navigate to the Videos page
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