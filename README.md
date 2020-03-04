# Milestone Project: Pixie Games

This project focuses on the website development for an e-commerce store that sells games and allows users to leave reviews. The website is designed to be intuitive and easy to navigate. It is targeted towards users interested in purchasing games and being involved in the community. 

## Demo

A live demo of the website can be found here: https://django-angie.herokuapp.com/home/


## Project Strategy and Scope
### User Stories

| User Stories        | Description           | Features to implement  |
| :------------- |:-------------| :-----|
| 1      | User would like to know more about the game they are about to purchase. | To include essential information such as the publisher's name, price of the game, release date, etc.  |
| 2      | User would like to know more about the game. | To include an about section that gives more information about the game.  |
| 3      | User would like to purchase the games of their choosing. | To include an add to cart button that allows users to add their games to cart.  |
| 4      | User would like to review their items before they make the purchase. | To include a view cart page that displays all the games that the user has added to the cart.  |
| 5      | User would like to add or reduce the number of copies of a particular game . | To include a add and reduce option for users to buy more copies or reduce the quantity when they click the add or minus buttons.  |
| 6      | User would like to see the subtotal of their item. | To include a subtotal function that shows the final cost of an item(s) when users add quantity or buy more than one game.  |
| 7      | User would like to go back to games catalog after reaching the cart | To include a button, linked to the games catalog page, next to the checkout. |
| 8      | User would like to add reviews  | To include a form that allows users to add reviews after they click the add reviews button. |

## Project Structure
### (i) Overview
- Homepage - The homepage has a slideshow that showcases games sold on the website. Below that, there is a short description of the website and how the users can interact with it. There is also a collapsible navigation bar (hamburger menu) on the right-hand side of the website. 

- Game Catalog Page - The games catalog page showcases all the games sold on the website.

- Cart - Games can be reviewed by the user before the user is ready to complete their purchase. 

- Community Reviews - This page allows logged in users to leave reviews and unregistered users to read reviews posted.

### (ii) Wireframes here.

View wireframes for both desktop and mobile here: https://docs.google.com/document/d/1EXbarzoNlgPHfAAtar7pMNcObNwsNRzCSKVN2oFSOc8/edit?usp=sharing

## Project Skeleton
### (i) Existing Features
- Homepage - The slideshow gives users a peek into the games sold at the site. Additionally, the short introduction of the website gives users a little more detail about how to go about using the site.  There is a collapsible  navigation bar on the top-right hand corner of the homepage. This was placed to give users easier access to navigate the different pages easily and quickly. Upon clicking the icon, the icon will open a full screen overlay for users to see the different pages in the website. 

- Games Catalog - Bootstrap features such as cards were used to display information about each of the games sold on the site. Some of the information includes title, price, category, publisher, release date, etc. This will give users more information about the game before they add the game(s) to cart. User authentication  only allows logged in users to add games to cart, after which they will see a message pop-up that indicates that the game has been successfully added to the cart. Additionally, only the admin or superuser is able to create, edit, delete games. 

- Cart/View Cart - Only logged in users will be able to add games to their cart and view their cart before completing their purchase. Clicking on the view cart button will allow logged in users to view their cart and allow them to add or reduce their cart for each item. When reducing or adding more copies of the game on the view cart page, the users will be able to see the subtotal as soon as they add or reduce their items. 

- Checkout - Logged in users will then be able to checkout their items as soon as they are satisfied with their selections. Once they click on checkout, they will be redirected to stripe payment to complete their purchase. Once the payment is successful, a message will popup to show that the payment was successful and a unique steam ID has been sent to their email. 

- Community Reviews - Only admin/superuser will be able to delete reviews. Unregistered users can see user reviews but will not be able to leave reviews. 

### (ii) Features to implement in the future
In the future, I would like to create a function for the unique steam ID to be sent to the users email address once they have successfully completed payment. 

I would also like to include an option to edit and update reviews. 

Another feature to implement in the future includes allowing registered and logged in users who have created their reviews to only edit and update their reviews - they will not be able to edit other users' reviews. 

There should also be a contact form or form of contact that allows users to reach out via social media or directly to the admin. 

Finally, I would like to include a profile page that allows users to access their profile, upload pictures, see their username and password. Registered users will also be able to edit, update and delete their profile. 

###Limitation 
After checkout, users are only prompted with a message that they have completed their purchase successfully. No email confirmation is sent to their email address.

## Project Surface
### Design Choices
(i) The color scheme of bright blue and black creates contrast to make it more eye-catching and outstanding to users. I also believe that the colour scheme appeals to users.

(ii) The font was chosen to reflect a more "techy" feel of the website.

(iii) Background image is black so that it doesn't distract users from the games displayed on the website.

## Technologies

1. HTML — used to structure the content of the website (link to the documentation: https://devdocs.io/html/)
2. CSS — used for styling the website (link to the documentation: https://devdocs.io/css/)
3. Jinja — used for styling (link to the documentation: https://jinja.palletsprojects.com/en/2.11.x/)
3. Bootstrap (link to the documentation: https://getbootstrap.com)
4. Javascript — for the navigation bar (link to the documentation: https://devdocs.io/jsdoc/)
5. Python3 — (link to the documentation: https://docs.python.org/3/)
6. Django — (link to the documentation: https://docs.djangoproject.com/en/3.0/)


## Testing
(i) Mobile Responsiveness

This site was tested across multiple devices multiple mobile devices 
(iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy) to ensure compatibility and responsiveness.)

Website tested on mobile and on laptop mode : https://drive.google.com/drive/folders/1-eJxjByE_b5XR4rv-MGpQLcyzqR0ku33?usp=sharing

(ii) Browser Compatibility

This site was tested across multiple devices multiple mobile devices 
(iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy) to ensure compatibility and responsiveness.)

(iii) User authentication restricts access and allows superusers/admin to create, edit and delete games. They will also be able to delete reviews.

(iv) User authentication restricts access and allows logged in users to add games to cart and create reviews. 

(v) Test Cases 

| Test Case(s)        | Description           | Outcome |
| :------------- |:-------------| :-----|
| 1      | When a user clicks on the Happy Browsing button on the bottom of the homepage, they will be redirected to the games catalog page. | Pass  |
| 2      | When user clicks on the hamburger icon, it will open a full-screen overlay to display the pages on the website. | Pass  |
| 3      | When superuser clicks on the create game button, they will be redirected to a form that allows them to create a game. | Pass  |
| 4      | When superuser clicks on the edit or delete button, they are able to update the game and delete it if they choose to. | Pass  |
| 5      | When a logged in user clicks add to cart, they will be able to view cart and review their purchase | Pass  |
| 6      | Registered users want to add or reduce items in carts. | Pass  |
| 7      |Registered users can view the subtotal of items.| Pass  |
| 8      |Registered users can checkout items and complete payment for their purchase.| Pass  |
| 9     |Images throughout the website are responsive.| Pass  |



## Bugs Discovered
No bugs found. 

### Media 

All images and game content were taken from https://store.steampowered.com/. 
All rights go to Steam, a video game digital distribution service by Valve.

### Acknowledgements

W3Schools:

1. Used an overlay for the navigation bar from W3Schools: https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_overlay
2. Used responsive images from W3Schools: https://www.w3schools.com/howto/howto_css_image_responsive.asp

Bootstrap features: 

1. Used cards for the about page of the website : https://getbootstrap.com/docs/4.3/components/card/
2. Used carousel for the about page of the website: https://getbootstrap.com/docs/4.3/components/carousel/


Fonts:

https://fonts.google.com.

Stackoverflow for debugging and other programming questions:

https://stackoverflow.com/

