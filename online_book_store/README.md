# Eunoia's Store  
An online book store.
  
## Dependencies
1. Python3
2. Flask
3. Sqlite3
4. Bootstrap-3
5. Jinja2

## Setting up the environment
    # Install the dependencies by running "pip3 install -r requirements.txt"

## Initializing the Database

    # Create DB tables and populate them using the below command:
    python3 init_database.py


## Running the app

    # Start the Flask development web server
    python3 app.py
    
    # Enter http://127.0.0.1:5000/ in the browser and enjoy browsing the store!

    # To access the manager pages, use :
    username : 'admin'   
    password : 'password'   

## System Functionalities

### 1. User Registration and Login                                                                                             
    New users will be able to register themselves on the online platform by providing the required details and after successful registration, the users have to login and logout using the username and password every time they need to access the platform.

    To try this functionality, logout in case you are logged in (follow feature #20).
    Then click log-in button which will be visible on the right corner of the navigation bar.
    In case you want to login as a manager, click on the sign in as a manager.
    And in case you want to register as a new user, click on the sign up link given at the bottom of the login page.

### 2. Manager Accounts                                                                                                 
    The platform will also facilitate manager accounts. These accounts can add new books to the inventory and can also add new managers to the platform.

    This can be tried out by first, logging in as a manager, use the account dropdown component which is located on the top-right corner of the navigation bar. Then click 'add managers'.

### 3. Make orders for books                                                                                             
    Users will be able to order multiple books at a time. They can order different books and/or they can also order multiple copies of one book.

    This can be done by first browsing the books(follow feature #9) and then click on the required book and in the product page of the book, click add to cart and then manage you item in the cart (follow feature #15) and click 'place order' after selecting one or many cart items.
    You will be redirected to the 'order placed' page.
### 4. Add new books                                                                                    
    Manager accounts can add new books to the store which did not exist previously  by entering the details of the book. The details include publisher, author, title, date of publishing, language, price, ISBN etc...

    This can be tried out by first, logging in as a manager, use the account dropdown component which is located on the top-right corner of the navigation bar. Then you can choose add new books and add new books.
### 5. Bulk Inward a batch of books                                                                                                 
    When a bulk stock comes into the store for instance from a publisher, the managers can update the inventory levels of all the inwarded books using this feature.

    To do this, login as the manager and use the drop down menu at the top right of the navigation bar.

    This can be tried out by first, logging in as a manager, use the account dropdown component which is located on the top-right corner of the navigation bar. Then you can choose bulk inward and perform inwarding.

### 6. Bulk Outward a batch of books                                                                                                 
    When a bulk stock needs to be outwarded from the store for instance when there is misprint in the copies or the books are damaged, the managers can update the inventory levels of all the outward books using this feature.

    This can be tried out by first, logging in as a manager, use the account dropdown component which is located on the top-right corner of the navigation bar. Then you can choose bulk outward and perform outwarding.

### 7. Book ratings and reviews                                                                                         
    Users can rate and comment on the books they have read or are interested to rate or comment about. They can give a rating between 0 to 10 where 10 means the book is awesome and they can leave a short comment. One user will be able to comment only once per book and can edit the comment whenever they want to.

    To try this out, first login as a user, then navigate to any of the product pages (follow feature #19) and then click on "write a review" to rate the book and/or also give a review on the book.


### 8. Vote Reviews for usefulness                                                                                        
    The users can rate the reviews left by other users by choosing one the following categories of rating: useless, useful or very useful. This rating will help other users to get the right reviews about the books.

    This can be used by first logging in as a user and then navigating to the product page (follow feature #19) and then scroll down the reviews section. Here, you can rate any of the reviews by clicking on the bottom right buttons. You can also change your vote,

###  9. Browse books in the store                                                                                      
    Users will be able to browse books in the store-front and filter books based on author, title words, language and publisher.

    This can be tried out on the home page of the website. 
    Fill zero or more search by fields with partial or full words and select one of the sort by option and click on search.

    If none of the fields have been filled then all the books in the store will be displayed, else search results will be displayed.
    
### 10. Public User Page                                                                                                 
    Anyone will be able to look at the user page of a particular user without logging in. In this page, they can view all the reviews given by the user and also vote for usefulness and as well as mark them as trustful or not-trustful.

    You can access these pages either from the "top users" page link or from link in reviews under any of the products pages.
    You can also access user page with the following url:
    'http://127.0.0.1:5000/user/<username>'
### 11. Mark users as trustable                                                                                                
    Users can mark other users as trustable. One user can declare any number of users as trustable and these trust statistics will be used to deliver better personal recommendations for the users 

    You can mark users as trust/non-trustable by navigation to the user page (as shown in feature #10) and then click on "trust" or "non-trust" feature displayed under the username. You can also change your choice. 
### 12. Filter comments                                                                                                
    Users will be able to filter comments for any book they are browsing based on the usefulness score of the comments. The number of comments to be shown can also be chosen as either 5 or 10. 

    Navigate to the product page by following the instructions given in feature #19 and scroll down to the reviews section.
    Then use the filter dropdowns and click on "filter" to filter the results.
### 13. Recommendations                                                                                                
    Users will be able to view recommendations based on the current book they are browsing. The recommendations will be based on the book orders of the other users who have also ordered the book being currently browsed. More priority will be given to books which have higher sales.

    Navigate to the product page by following the instructions given in feature #19 and scroll down to the recommendations section.
    If there are no recommendations, then the section will not be visible.

### 14. Update personal details and change password                                                                                                  
    Users of the platform will also be able to modify their personal details and also change their password for security reasons.

    This can be tried out by first, logging in as a user, use the account dropdown component which is located on the top-right corner of the navigation bar. Then you can choose any of the choices.     

### 15. Cart Management

    The items added to cart can be managed by either increasing the quantities, decreasing the quantities or removing them.

    This can be tried out by first, logging in as a user, use the account dropdown component which is located on the top-right corner of the navigation bar. Then click on 'cart' and then you can change the quantities of the items(if any) present in the cart. To delete an item, change the quantity to 0 and when an order is placed, items are removed from the cart.    
### 16.  Book statistics                                                                                               
    The platform will showcase ‘n’ most popular books , ‘n’ most popular authors and ‘n’ most popular publishers based on the sales of the books. An user will be able to choose the value of n to view the statistics.
    
    This can be viewed by clicking on 'Top Charts' tab on the navigation bar in the website.

### 2.17.  User awards                                                                                              
    The book store also maintains leaderboards for the ‘n’ most trusted users and ‘n’ most useful users so that they can be awarded and incentivised for their community contributions. Truster is the one who trusts the user, Trustee. Trustee is the user who is trusted.

    This can be viewed by clicking on 'user awards' tab on the navigation bar in the website.

### 18. Role-specific Restricted access

    The managers cannot access user specific pages and the users cannot access manager specific pages and non-logged in users cannot access either of them. When tried to access, it will redirect the user or manager to the login page.

    To try this out, logout and try to access "http://127.0.0.1:5000/account/profile/update". This will redirect you to the login page
### 19. Product Page

    Product page has 3 sections.
    First is the details section which gives each and every detail about the book.
    Below this is the add to cart option.
    Second is the recommendations section and third is the recommendations section.

    You can access the product pages either from clicking the search results or using the below url:
    'http://127.0.0.1:5000/product/<isbn>'
### 20 Logout and Session Management
    
    The user will be logged in for a specific period of time, even if the user closes the website and opens it again. The user or manager can also logout when they are done using it. 

    This can be tried out by first, logging in as a user, use the account dropdown component which is located on the top-right corner of the navigation bar. Click on the 'logout' feature.    