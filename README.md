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

* As a first-time visitor, I want to immediately understand the app's main purpose
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

##### For all users

* A responsive fixed navbar displaying with the ability to navigate to all the site's main pages, register for an account, log in/out and view the total value of the user's shopping cart
    * The main navbar is accessible via a hamburger menu in the top left of the viewport on mobile and tablet devices
* A search bar for the store in which users can input text and find items whose names contain the search string
    * If no products are found, a button to view all products appears in the middle of the page to redirect the user back to the shop's main page
* A call to action button on the homepage that invites the user to subscribe and takes them to the subscribe page, where they can choose one of three packages
    * If a user selects a subscription to purchase, they must log in before being redirected to the checkout page for that subscription
* A shop page displaying all items in store and the total number of items
    * In the shop dropdown menu, the user can select individual categories which filters the items and only shows those belonging to the category in the link. The number of items shown updates accordingly
* A sorting box above the shop items for the user to sort by name, price and rating, in both ascending and descending order
* An image of each product in the store with its name, price, category and rating below. The user can click the image to be taken to that product's individual page where they can select the size (if applicable) and quantity of the item before adding it to their cart
* A continue shopping button on each product's individual page to take the user back to the main shop page
* An add to cart button below each product on the shop's main page that triggers a modal for the user to select size and quantity. This is more user-friendly than trying to fit a quantity form and size selector below each item.
* A contact form that users can fill out to submit a query and receive a confirmation e-mail that their request has been received.
* A real-time cart total that can be clicked on to bring up a preview of the items in the user's cart
* A cart page that lists all the items in the user's cart and keeps a running subtotal, and calculates the total, delivery, grand total, and how much more the user can spend to get free delivery
    * The user can also update the quantity of an item in their cart on this page, or remove it from their cart entirely
* A checkout page where the user enter their billing and shipping information, and check out securely using Stripe
* A footer that displays social media icons, copyright info and 'Contact Us' text, that takes the user back to the contact page
* A pop up box providing user feedback depending on the action taken e.g. adding an item to the cart triggers a success message that a specified quantity of an item in a certain size was added to the user's cart
* Validation errors that appear in red if a field in a form is not filled out correctly
* A 404 page that is rendered if the user enters an invalid URL
* An automatic redirect to the login page using the @login_required decorator if the user attempts to access a URL that only logged in users can see
* An automatic redirect to the home page if the user attempts to access a URL that they are not authorised to view

##### For registered users

* A user dashboard where the user can see their current subscriptions (if any)
* A profile page where the user can view and update their account details and their order history, and delete their account
* A link in each order of the user's order history that takes the user to a page where they can view an order in more detail
* A form for updating the user's account details
* A checkbox when checking out with a susbcription or shop order that the user can check to save their information to their profile for future orders

##### For members (paid subscribers)

* A videos page where the user can view the training videos available to members
    * Each video comes with a title, duration, rating and description
* Certain videos are only available to premium members, depending on the boolean value of the premium field in the Video model
    * Basic plan members are redirected back to the main videos page if attempting to manually access a URL for a premium video with an error message that they must purchase a premium or VIP package to be able to view these
* A search bar at the top of the videos page in which users can input text and find videos whose titles or descriptions contain the search string
    * A filter is in place so that the search will never return premium videos to basic members
* A sorting box above the videos for the member to sort by title, length and rating, in both ascending and descending order
* An individual page for each video, including a comments section for members to leave comments and interact with other members
    * Comments must be approved by an administrator and are visible to other members once approved
    * Before the comments thread, the number of total comments is shown and updates in real time when a comment is approved or deleted
* The opportunity for users to edit and delete their approved comments
    * If a member edits their comment, it must be approved again before others can see it
* VIP members receive 50% off in the store and free delivery on all orders
    * On the shop page, an item's usual price is struck through with a line and the VIP's discounted price is shown

##### For administrators (superusers)

* A button to add videos or store items on the videos and shop pages respectively
* An admin panel page where the administrator can also perform the above two actions
* The ability to approve or reject comments made by other users
* The ability to edit or delete comments made by other users, in case of inappropriate content
* A modal trigger that asks the administrator to confirm whether they wish to delete or reject a comment, with a cancel button in case they mistakenly selected this option

#### Features left to implement

* Pagination for shop products, videos, comments and user order history to limit the number of items on each page so that the user doesn't have to scroll too far to locate a record
    * The user could also choose how many search results they would like per page, e.g. 20, 50, 100
* The ability for users to freeze, unfreeze, upgrade or downgrade subscriptions
    * Freezing a subscription would simply set the active field in the Subscription model to false, and the user would not have access to the materials in this time
    * Unfreezing the subscription would set the active field back to true, and the user would be able to access the materials again
* A product review system on each product page where users could leave a descriptive review and a rating of a product
    * These would be laid out in the same way as video comments, with an administrator having to approve or reject a review
    * Each review could also have like/dislike buttons so that users could sort reviews by helpfulness 
* A forum where users can interact with each other, share their progress and even engage in general chat
    * This is a more comfortable space for genuine user interaction than the comments section of a video
* A like and dislike button on each video comment that members can click to show their approval or disapproval at another person's comment
    * It could then be possible to sort comments on a video by the number of likes received
* A recurring payment system where paid subscribers are automatically charged at the end of each billing cycle
* The ability to publicly view other user/member profiles and their contribution history
    * Other users/members may wish to hide potentially sensitive data such as e-mail addresses from other users, so they could have the option to not allow this to be seen by others
* A private messaging function that would enable users to communicate with each other on the app itself
* An FAQs page that a user could read before potentially submitting a contact form with a query already asked many times
* A more personalised and interesting custom 404 page

[Back to TOC](#table-of-contents)

### Technologies Used

**Backend**
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

**Frontend**
* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

The following frameworks, libraries and packages were also used:

**Web frameworks**

* [Django](https://www.djangoproject.com/): the app's core web framework
* [Stripe](https://www.stripe.com/): an API framework for secure payment processing
* [Amazon Web Services (AWS)](https://aws.amazon.com/): for cloud-based storage of static and media files, namely [S3](https://aws.amazon.com/s3/) and [IAM](https://aws.amazon.com/iam/)

**Databases**

* [Postgres](https://www.postgresql.org/): a server-based RDBMS

**Dependencies**

* [django-allauth](https://django-allauth.readthedocs.io/en/latest/): for user authentication
* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/): for elegant and responsive rendering of forms on the front end
* [Django Countries](https://djangopackages.org/grids/g/countries/): for the implementation of a dropdown menu containing all recognised countries and territories
* [django-storages](https://django-storages.readthedocs.io/en/latest/): to connect Django to S3
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html/): a SDK by AWS for Python that allows Django to connect to S3
* [dj-database-url](https://pypi.org/project/dj-database-url/): to enable use of Postgres
* [psycopg2-binary](https://pypi.org/project/psycopg2-binary/): a database adapter to connect Postgres to Python
* [dj-stripe](https://dj-stripe.readthedocs.io/en/master/): for the implementation of Stripe models within the Django framework
* [Gunicorn](https://gunicorn.org/): a WSGI server that acts as the application's server when it is deployed to Heroku
* [JSON](https://www.json.org/json-en.html): for local data storage and easy loading of data to the Django admin 
* [Pillow](https://pillow.readthedocs.io/en/stable/): to enable the use of the image field in the database
* [Coverage](https://coverage.readthedocs.io/en/coverage-5.5/): to determine how much of the application's code has been tested
* [pytz](https://pypi.org/project/pytz/): for cross-timezone synchronisation

**Frontend libraries and frameworks**
* [jQuery](https://jquery.com): to simplify DOM manipulation and event-handling
* [jQuery UI](https://jqueryui.com/): for autocomplete options in the site's search bar
* [Bootstrap](https://getbootstrap.com/): for site responsiveness and clean, intuitive layout
* [Google Fonts](https://fonts.google.com/): to import font families to be used for the application's front end
* [Font Awesome](https://fontawesome.com/): for responsive icons that let users initiate actions 
* [Favicon](https://favicon.io/): to include a favicon within the browser tab
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools): to test responsiveness, inspect the role of each element and 
class and experiment in real time with new style rules and their effect on the site's layout and structure
* [Google reCAPTCHA](https://www.google.com/recaptcha/about/): for determination of human access to the application

**Software hosting and cloud platforms**
* [Heroku](https://www.heroku.com/): for the project's live deployment
* [GitHub](https://github.com/lbacon17/lb_fitness): to create a repository for the project and link it to Heroku to be deployed
* [Gitpod](https://gitpod.io): to manage the project's necessary files and write the code for the project

**Design tools**
* [Am I responsive](http://ami.responsivedesign.is/): for testing and screenshots of the website's responsive design

**Validators**
* [PEP8](http://pep8online.com/): Python
* [JSHint](https://jshint.com/): JavaScript
* [Jigsaw](https://jigsaw.w3.org/): CSS
* [W3C](https://validator.w3.org/): HTML

**Other**
* [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/): for the app's secret key

[Back to TOC](#table-of-contents)

### Data Structure

The project uses Postgres as its database to store data in SQL format for the live site, which is visible in the Django admin panel. The data exists in a relational model.

[Back to TOC](#table-of-contents)

### Testing

To read about the testing process, please see the separate [TESTING.md](TESTING.md) file.

[Back to TOC](#table-of-contents)

### Deployment

To read about the deployment process, please see the separate [DEPLOYMENT.md](DEPLOYMENT.md) file.

[Back to TOC](#table-of-contents)

### Credits and Acknowledgements

[Back to TOC](#table-of-contents)
