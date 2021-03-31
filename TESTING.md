# **[LB Fitness](https://lb-fitness.herokuapp.com/)**

# Testing

This file documents the testing process of the project.

## Table of contents

* [Validation](#validation)
* [Responsiveness](#responsiveness)
* [Browser Compatibility](#browser-compatibility)
* [Testing User stories](#testing-user-stories)
* [Issues and bugs](#issues-and-bugs)

## [Back to README](README.md)

### Validation

#### Python

The code was passed through the [PEP8](https://pep8online.com/) validator. Four built-in lines in the settings file returned errors, these cannot be changed.

#### JavaScript

The code was passed through the [JSHint](https://jshint.com/) validator. No errors were found.

![JSHint validation](/libraries/code_validation/js_validation_jshint.png)

#### CSS

The code was passed through the [Jigsaw](https://jigsaw.w3.org/) validator. No errors were found.

![Jigsaw validation](/libraries/code_validation/css_validation_jigsaw.png)

#### HTML

The code was passed through the [W3](https://validator.w3.org/) validator. The validator returned several errors and warnings, all of which related to the use of template tags as attribute values. The validator also threw a number of fatal errors when coming across for loops. Removing these from the direct input allowed validation to continue, and no further errors were shown other than those of the nature mentioned.

As the causes of the warnings enhance rather than hinder the application's performance, and it would not be possible to connect the back and front end of the application without them, these can be ignored.

To view sample screenshots of HTML validation, please see the [HTML](libraries/code_validation/html) subfolder in the [Libraries](libraries/code_validation) directory.

[Back to TOC](#table-of-contents)

### Responsiveness

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

Smooth scroll behaviour is not supported on Safari, meaning the page jumps right back to the top when the return to top button is clicked as opposed to a smooth scrolling motion. This is due to Safari not supporting the scroll-behavior: smooth CSS property. I tried various JavaScript solutions to remedy this, but none of them had any effect. As this is a minor issue, I decided to take no further action at this stage.

[Back to TOC](#table-of-contents)

### Testing User stories

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

* As a user, I want to be able to search for products in the store using keywords so that I can potentially purchase some and see the number of results my query returned
    * I enter a search term in the search field within the navbar and am redirected to the shop page that displays all the results containing my search parameter along with the number of items found
    * If my search query returned no items, I can click a button to view all the shop's products so I don't have to come off the shop page or scroll back to the top of the screen to enter another query
* As a user, I want to be able to filter products in the store according to category
    * In the Shop dropdown menu, I navigate to the cateogry I want to browse and click on it
    * The page now only displays items in the selected category, and tells me how many currently exist
* As a member, I want to be able to search for material that I have access to so that I can easily find what I'm looking for and see the number of results my query returned
    * I navigate to the Videos page, enter a search term in the search bar above the videos and am shown all the videos that contain my search parameter along with the number of items found, with a button to view all videos
    * If my search query returned no items, I can either click a button to view all videos or enter another query in the search bar
* As a user, I want to be able to sort products according to different criteria such as name and price, so that I can find what I want easier or see what has the most recommendations
    * I navigate to the Shop page, selecting either all items or a certain category, and click the Sort by.. dropdown menu to see my sorting options
    * I select what criteria I want to sort by and the page automatically re-orders the items for me
* As a member, I want to be able to sort videos according to different criteria such as length and rating
    * I navigate to the Videos page and click the Sort by.. dropdown menu to see my sorting options
    * I select what criteria I want to sort by and the page automatically re-orders the items for me
* As a user, I want to be able to read about a product’s individual details
    * I navigate to the Shop page and click on a product's image, where I can see its name, price, rating and the category it belongs to
        * In future versions of this app, this page would also contain a product description to give the user more information
* As a user, I want to contact the site owner with a question and recieve a confirmation e-mail that my query has been received
    * I click on Contact in the navbar to navigate to the Contact page and fill out the contact form, entering my name, e-mail address, the subject of my query and a message, and click Submit
    * I receive a confirmation e-mail containing the contents of my query and assurance that the site owner will answer me as soon as possible
    * I'm also redirected back to the Contact page with a notification that my query has been sent and the form has been cleared
* As a user of the app, I want to read about its owner and find out more about the business
    * I click on the About link in the navbar and can read further information about the site and the app's story

**Administrator**

* As an administrator, I want to add a product to the store
    * I navigate to the Shop page and click the Add Item button next to the sorting menu
    * I enter the details of the new product in the form, making sure to fill out all fields correctly, and click Add Product
    * I receive a notification that the product has been successfully added and am redirected to the new product's page, where I can see its details
    * I can also add a product via the Admin Panel, by selecting this from the My Profile dropdown menu and clicking the Add Store Item button
* As an administrator, I want to edit a product’s specifications or update its details
    * I navigate to the Shop page and click the Edit button by the product I want to update
    * I fill out the product form making the necessary changes and click Update Item
    * I receive a notification that the details have been successfully updated, and am redirected back to the product's page
* As an administrator, I want to delete a product from the store
    * I navigate to the Shop page and click the Delete button by the product I want to delete
    * A pop-up box appears and I can click Cancel in case I accidentally selected this action, which will safely take me back to the page I was on
    * If I am sure I want to delete this product, I confirm this action by clicking Delete again, and receive a notification that the item has been successfully deleted from the store before being redirected to the main Shop page
* As an administrator, I want to add a video to the site that is accessible to members
    * I navigate to the Videos page and click the Add Video button next to the sorting menu
    * I enter the details of the new video in the form, making sure to fill out all fields correctly, and click Upload Video
    * I receive a notification that the video has been successfully added and am redirected to the new video's page, where I can see its details
    * I can also add a video via the Admin Panel, by selecting this from the My Profile dropdown menu and clicking the Add Training Video button
* As an administrator, I want to edit a video's details such as replacing its actual file, updating its title or description or fixing an incorrect value for its duration
    * I navigate to the Videos page and click the Edit button by the video I want to update
    * I fill out the form making the necessary changes and click Update Video
    * I receive a notification that the information has been successfully updated, and am redirected back to the main Videos page
* As an administrator, I want to categorise videos so that some are only accessible to premium members
    * I navigate to the form to add or update a video, and select the Premium checkbox at the bottom of the form
    * If checked, this video will only be available to members on the Premium or VIP plans - members on the Basic plan will not be able to see it won't show up in their search results
        * If they try to access the video by its URL, they will be redirected with an error message that they must upgrade their subscription to view this content
* As an administrator, I want to delete a video from the database
    * I navigate to the Videos page and click the Delete button by the video I want to delete
    * A pop-up box appears and I can click Cancel in case I accidentally selected this action, which will safely take me back to the page I was on
    * If I am sure I want to delete this video, I confirm this action by clicking Delete again, and receive a notification that the video has been successfully deleted before being redirected to the Videos page
* As an administrator, I want to be able to approve or reject comments on videos by users so that all content on the site remains appropriate and makes for an enjoyable experience for all members
    * I navigate to a video's individual page where, if a user has made a comment, it will appear at the top of the comments section under the Comments pending approval heading
    * To approve the comment, I click approve and receive a notification that the comment was successfully approved
        * The comment now appears in the comments section and the comment counter is incremented by one
    * To reject the comment, I click Reject, which triggers a pop-up asking me to confirm the rejection of the comment
    * If I accidentally clicked Reject, I can click Cancel which dismisses the pop-up and takes me back to the video's page
    * To confirm rejection, I click Reject again and receive a notification that the comment was successfully rejected
        * The comment now no longer exists in the database and will never appear anywhere

[Back to TOC](#table-of-contents)

### Issues and Bugs

During testing the following bugs were noted:

* **Bug**: logged in users were able to access other user's dashboards, profile pages and training material without a subscription by typing in the relevant URL path.
* **Fix **: I used various if statements to handle these errors, the overarching theme being Django checking that the user's ID or username matches the parameter passed into the URL. If it doesn't, it will throw an error and redirect the user to the homepage. Here is an example in the user_dashboard view that shows what happens when a user tries to access a dashboard that does not belong to them:

```
    @login_required
    def user_dashboard(request, username):
        """This view renders the individual user's dashboard when logged in"""
        user = get_object_or_404(User, username=request.user)
        videos = Video.objects.all()
        if user.username != username:
            messages.error(request, "You do not have permission to view " \
                "another user's dashboard.")
            return redirect(reverse('home'))
```

* **Bug**: an ImportError occured due to a circular import, where the models file in the members app was importing the Package model from the subscribe app, while the models file in the subscribe app was importing the Member model from members.
* **Fix**: I resolved this issue by moving ```from members.models import Member``` inside the Subscription model, as it was only needed there.

* **Bug**: when trying to get select a subscription, the app wouldn't recognise which subscription was selected when checking out, and the subscription details would in turn not render on the user's dashboard, and the user would not gain access to the subscription material 
* **Fix**: to resolve the issue, I made the process of selecting a subscription package identical to the process of adding item to the shopping cart, except this wouldn't be rendered on the page. The solution was two-fold:
    1. First, I created the add_package_to_cart view and wrapped the Get Plan buttons on the subscription page in a form whose action was to call that view
    1. This caused the issue of redirecting to the same page due to the presence of a hidden input field with the redirect_url name. To solve the issue, I changed its value to the get_subscription view, passing in the package ID as an argument:

    ```
        <form action="{% url 'add_package_to_cart' package.id %}" method="POST">
            {% csrf_token %}
            <input type="submit" class="btn-lg btn-success text-dec-none" value="Get Plan">
            <input type="hidden" name="redirect_url" value="{% url 'get_subscription' package.id %}">
        </form>
    ```

* **Bug**: trying to prevent users from accessing the subscribe page was problematic, as using the request.user.member path would throw an error when a non-susbcriber tried to access the page. Using an ```if request.user.is_authenticated``` statement only helped users not logged in see the page, but the same error would be returned when they logged in to get a subscription. 
* **Fix**: I used the filter method to fetch an object from member that only returned the existing user's username in the user field. If it returned a result, that would mean the user already had a subscription, so a code block would run that redirected the user back to the homepage. If the member variable doesn't exist, the user is free to purchase a subscription.

```
    if request.user.is_authenticated:
        member = Member.objects.filter(user=request.user)
        if member:
            messages.error(request, 'You already have a subscription.')
            return redirect(reverse('home'))
        else:
            context = {
                'packages': packages,
                'member': member,
            }
            return render(request, 'subscribe/subscribe.html', context)
```

* **Bug**: if a user clicked on a subscription to purchase, it was added to their cart, but if they left the page and went back to select another subscription, the original subscription remained in the cart and the user was charged for both. Although the quantity of a subscription is always set to 1, there was nothing to stop one of each package being stored in the cart.
* **Fix**: to solve the issue, I stored the cart information in a variable at the start of the add_package_to_cart to cart view and made an if statement where the app would look for the cart, and clear it if it existed. This meant that each time the user clicked on a subscription package, anything already in the subscription cart was removed.

```
    @login_required
def add_package_to_cart(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    subscription_cart = request.session.get('subscription_cart', {})
    if subscription_cart:
        subscription_cart.clear()
        if package_id in list(subscription_cart.keys()):
            subscription_cart[package_id] += quantity
        else:
            subscription_cart[package_id] = quantity
    else:
        if package_id in list(subscription_cart.keys()):
            subscription_cart[package_id] += quantity
        else:
            subscription_cart[package_id] = quantity

    request.session['subscription_cart'] = subscription_cart
    return redirect(reverse('get_subscription', args=[package.id]))
```

* **Bug**: I created a separate Stripe webhook handler for the subscribe app called StripeWH_Handler_Subscribe, but this caused an internal server error.
* **Fix**: the error seemed to be caused by the double underscore, so I simply re-named the handler to StripeWH_HandlerSubscribe, which solved the issue.

* **Bug**: When updating the quantity of an item with sizes in the shopping cart, the size would disappear after the update.
* **Fix**: After some research, I discovered that the hidden input field with the name of "item_size" was missing from the quantity form. Inserting it solved the issue.

### Unsolved Bugs

* **Bug**: VIP users receive a 50% shop discount and free delivery in the app. Currently, all store items show the discounted price and the cart's total is calculated correctly, yet after checking out, the full price is shown in the order confirmation and shows up like this in the admin panel. The user is also charged for delivery if the order is under £50. However, the correct amount is shown in the Stripe payment history.
    * I have tried many things to fix this bug, most notably trying to halve the aggregated lineitems total in the ShopOrder model if the user is a VIP, and adding an is_vip field to the Member model, but this has not worked. The one solution that succeeded in halving the price for VIPs also halved the price for other users, as the if condition was actually just checking that a VIP existed in the database, rather than if that user was a VIP. Trying to match the VIP and the user also threw 404 errors when trying to load the shopping cart and check out, and I decided that implementing any of these alternatives would make the app worse.

* **Bug**: I have implemented the ability to rate a video and store the video's rating in the database, but not yet been able to work out an average value of all the ratings for a video. For example, if one user is logged in and rates a video as 4 stars, the video's rating will be saved in the database as 4. However, if another user then rates the video as 2 stars, the app changes the rating to 2 rather than calculate the average of 3. In other words, the app only saves the most recent rating. 
    * The closest I came to saving this issue worked out the average rating across all videos in the app, rather than just one. I have still decided to leave this component in as I feel that it is a nice feature for the site to have and makes it more user-friendly. I would also like to implement this for the shop's products in future iterations. Unfortunately, time did not allow this before the submission deadline.

* **Bug**: Payment intents don't succeed when the user checks out with a subscription, but do when they check out from the store. Each checkout requires a separate endpoint, and Stripe sends webhooks to all endpoints by default. Although the payment intent doesn't succeed with Stripe, the subscription still appears in the Django admin with the correct amount, and the user gains access to the subscription material.
    * Several tutor sessions did not manage to resolve this issue. Although this would obviously be an issue if this were a real store, I feel it is better to leave this issue unsolved in the testing phase to demonstrate the app's functionality and the possibility to give a user further access to the site when completing a purchase.

[Back to TOC](#table-of-contents)

[Back to README](README.md)