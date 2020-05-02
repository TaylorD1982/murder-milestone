[![Build Status](https://travis-ci.org/TaylorD1982/murder-milestone.svg?branch=master)](https://travis-ci.org/TaylorD1982/murder-milestone)         ___        ______     ____ _                 _  ___  

<h1>Stiletto Murder Mysteries</h1>

<p>Stiletto Murder Mysteries is a company of actors and storytellers who organise Murder Mystery evenings throughout Scotland. The company has devised a number of scenarios, which they stage in hotels and castles accross the country with the participation of paying guests.</p>

<p>The purpose of this website is to allow prospective guests to view details of events, read & post reviews, check out the latest news and book tickets to the evening of their choice.  Vistitors to the site may also contact the company directly.</p> 

<h2>UX</h2>

<p>The site has a simple, clean, layout with a limited colour-scheme of black, dark blue and white contrasted with ocassional splashes of crimson. Posters specific to each event provide a contract to the sections of text, as do the star ratings in the review section.</p>
<p>The original design of the site is shown below. The final version is broadly the same although you will notice one or two changes.</p>  

<img src="{% static 'images/wire.png' %}" width="100%">

<h2>USER STORIES</h2>

<h5>Below are a number of scenarios, which demonstrate how a visitor would navigate through the site.</h5>  

<ol>
<li><p><b>David</b> visits the site and decides to find out what others thought of Stiletto Murder Mysteries. He navigates to the reivews section and sees that the top review was positive, giving the evening a 4-star rating. He clicks on the 'Full Review' button and is taken to another page showing the feedback in its entirety.</p></li> 

<li><p><b>Emma</b> lives in Glasgow and is looking for an event in her city. She goes to the 'Murder Mysteries' page on the site and scrolls down to find a party in that location. The event 'The Hunting Party' is being held in a hotel close to her next month and she decides this would be perfect, so she clicks on the 'Register' button in the Navigation Bar. Once she has registered, she returns to the 'Murder Mysteries' page and adds 3 tickets to her cart. She checks that the details are correct ands then proceeds to the checkout, were she enters her payment details and books the 3 tickets for her event.</p></li> 

<li><p><b>Colin</b> attended an event “A Time to Kill” with a friend who had bought the tickets. Colin thought the production was a waste of money and would like to post a review warning others not to attend. He visits the site and navigates to the reviews page but discovers that he cannot post a review unless he is registered and logged into the site. He decides that he would prefer not to do so and leaves.</p></li> 

<li><p><b>Susan</b> has been asked to organise a murder mystery event as part of a team building exercise through work. The event must be private though, so simply purchasing tickets to a public event is not agreeable. She navigates to the “Contact” page on the site and completes the Contact Form, sending a query to the company detailing her requirements.</p></li>

<li><p><b>Nick</b> selects an event for himself and 5 friends to attend in Edinburgh next month. He is already logged in so he navigates to the cart and reviews his order. At this point, he realises that he forgot to get a ticket for himself, so he amend his order to 6 and then proceeds to the checkout, where he pays.</p></li> 

<li><p><b>Florence</b> is one of the principal actors with the Stiletto Murder Mysteries company. It is her job to update the news section of the site. She logs in to the 'admin' section of the site and clicks to add a post to the 'Blog' section. Here she adds a title of the post, some content and clicks to publish the company's latest update.</p></li>
</ol>



<h2>Features</h2>

<h3>Existing Features</h3>

<ul>
<li><b>Feature 1 (Navbar)</b> - The navbar allows the user to navigate to the various pages that make up the app. It collapses into a ‘burger’ in smaller screen sizes.</li>
<li><b>Feature 2 (Murder Mysteries event description)</b> – The Murder Mysteries page lists all of Stiletto's upcoming events. For each item, the event's poster is displayed along with the date, time, address and price per ticket. Users may click on the 'Full Scenario' button which displays a modal with a full description of the scenario of the party in question. Users can also add a certain number of tickets to their cart from this page.</li>
<li><b>Feature 3 (Contact form)</b> – The contact form allows visitors to easily send an email to the administrators of the site. It is linked to a Gmail account using EmailJS.</li>
<li><b>Feature 4 (News)</b> – The website's administrator can post updates using a form in the admin section of the site. A snippet of each post can then be viewed on the 'News' page, with the full post available by clicking the 'Read More' button.</li> 
<li><b>Feature 5 (Write a Review)</b> – If a visitor is logged into the site, they have the option of posting a new review in the reviews page and assigning a star rating. This option is removed when the visitor is not logged in.</li> 
<li><b>Feature 6 (Read reviews)</b> – All visitors to the site can read the reviews posted in the reviews section. They can click on Full Review to view the entire post.</li> 
<li><b>Feature 7 (Review Response)</b> – The site's administrator has the option of posting a response to any review via the admin panel.</li> 
<li><b>Feature 8 (Search box)</b> – The search box allows visitors to search the site for product names matching certin keywords.</li> 
<li><b>Feature 9 (Register)</b> – Users must be registered in order to post reviews and purchase tickets to events. The register mechanism allows them to do so by confirming their email address and inputting a Username and Password.</li> 
<li><b>Feature 10 (Cart)</b> – Amend the quantity of tickets and remove the entire event from cart.</li> 
<li><b>Feature 11 (Social Media Links)</b> – Visitors can be directed to the companies social media accounts via icons on the banner and contact page.</li> 
<li><b>Feature 12 (reset password)</b> – Vistors can reset their password if they have forgotten this.</li>
</ul> 

<h3>Features Left to Implement</h3>

<ul>
<li>Inclusion of an average review score against each event in the 'Murder Mysteries' page.</li> 
<li>Post reviewers name against their review.</li>
<li>Search for key words in the event description.</li>
<li>Back button from the search page.</li>
</ul>


<h2>Technologies Used</h2>

<ul>
<li><b>JQuery</b> – Simplification of DOM manipulation.</li> 
<li><b>Google Fonts</b> – The typeface used throughout the site. </li>
<li><b>Bootstrap</b> – A front-end framework used throughout the site. </li>
<li><b>MS Paint</b> – Used to create the original design of the site and adjust some of the images.</li>
<li><b>Python</b> – Programming language used throughout the site.</li>
<li><b>HTML</b> – For the structure of the app</li>
<li><b>CSS</b> - CSS was used for Styling</li>
<li><b>JavaScript</b> - JavaScript for application controller</li>
<li><b>Google Chrome</b> - Used for browser and development tools</li>
<li><b>GitHub</b> - Repository hosted on GitHub</li>
<li><b>Heroku</b> -App hosted on Github Pages</li>
<li><b>Django</b> - Web framework</li>
</ul> 


<h2>Testing</h2>

<h5>Below is a series of practical tests of the website's functionality</h5>

<h3>Navigation Bar</h3>

<ul>
<li>User clicks on the each of the navigation bar items and is correctly taken to that page.</li> 
<li>When the user is logged out, the icons “Register” and “Log In” are displayed. When the user is logged in, the icon “Log Out is dsiplayed instead”</li>
<li>In mobile view, the navigation bar shrinks to a burger image. When clicked on, the navigation items are displayed in a Nav bar that drops down from below the site's banner.</li>
</ul>

<h3>Murder Mysteries</h3>

<ul>
<li>The upcoming events are displayed in date order, from soonest to latest. Clicking on the “Full Scenario” button displays a modal with a full description of the scenario for that particular mystery.</li>
<li>User clicks “Add” without entering a number into the “Tickets” field and recieves  a “Please fill in this field” message.</li>
<li>Users enters a figure into the “Tickets” field and clicks “Add”. This adds that order to the cart, which displays the number of tickets in the Navigation Bar.</li>
</ul>

<h3>Contact</h3>

<ul>
<li>Social Media icons on the left hand side of the page can be clicked on, and the user will be directed to the platform selected.</li>
<li>The contact form on the right can be completed. By clicking the “Send Message” button an email will be sent via EmailJS. If the user fails to complete any section of the form, a message will be displayed stating “Please fill in this field”.</li>
</ul>

<h3>News</h3>

<ul>
<li>News items are displayed in date order, with the most recent post shown first.</li> 
<li>When the user clicks on the “Read More” button, they are directed to the full post.</li>
<li>From this page, the user can click on the “Return to Blogs” button and is returned to the news page.</li>
</ul>

<h3>Reviews</h3>

<ul>
<li>Reviews are displayed in date order, with the most recent review displayed first.</li> 
<li>User clicks on the “Full Review” button and is directed to the page displaying the post in its entirety.</li>
<li>User clicks on the “Back Button” and is returned to the reviews page.</li>
<li>When user is logged out, they have no option to post a review. </li>
<li>When user is logged in, “Write a Review” button is displayed. </li>
<li>User clicks on “Write a Review” button and is directed to page with a form to complete. The first field has a drop down with 5 events to chose from. </li>
<li>The last field has a drop down with 5 possible ratings. </li>
<li>Failure to complete any section of the form will display a “Please fill in this field” message. </li>
<li>Clicking on the “Submit” button will post the review, with the rating rendered in stars. </li>
</ul>

<h3>Register</h3>

<ul>
<li>User is asked if they “Already have an account?”. By clicking on the “Sign in” button, they are taken to that page.</li>
<li>A form is displayed below. User completes all of the required fields and clicks “Register”. A success message is displayed that reads “You have successfully registered” and the user is automatically logged in.</li> 
<li>If the user fails to complete any field and a “Please fill in this field” message is displayed.</li>
</ul>

<h3>Log In / Log Out</h3>

<ul>
<li>User enters their email address and password, clicks on “Login” and is logged into the site.</li> 
<li>User enters incorrect password and receives message saying “Your username or password is incorrect”. User enters incorrect username and receives message saying “Your username or password is incorrect”. </li>
<li>User fails to enter complete both fields and recieves a message stating “Please fill in this field”.</li>
<li>User clicks “Reset Password” and is taken to the password-reset page, where they can enter their email address in the field provided. Clicking the “Reset Password” button without completing this field displays a message stating “Please fill in this field”.</li>
<li>User enters an email address and clicks “Reset Password” and receives a 'done' message.</li>
<li>User clicks “Log Out” in the navigation bar. User is logged out, redirected to the home page, and receives a message stating “You have successfully been logged out”.</li>
</ul>

<h3>Cart</h3>

<ul>
<li>User visits the Cart page when they have not yet added any items. The page displays a message saying “Your basket is empty”.</li>
<li>User adds one event ticket to the cart and visits the Cart page. User is shown details of their purchase including the name of the event, event details, price per ticket, number of tickets in cart and the total cost of the order. </li>
<li>User has the option to amend the number of tickets in the order. User changes number of tickets from 1 to 2 and clicks “Amend Quantity”. Number of tickets and total cost of order both update.</li>
<li>User wishes to remove this event from their cart. User clicks on the “Delete” button, all tickets are removed and page will display 1. “Your basket is empty”.</li>
<li>User adds 1 ticket from the event “A Time To Kill” and one ticket from the event “The Casino Killing” to their basket. They navigate to the cart. Details of the first event are shown above those of the second. The total cost of the order is displayed correctly at the fot of the page.</li>
<li>User amends the number of tickets for “A Time To Kill” from 1 to 2 and clicks “Amend Quantity”. Number of tickets for this event and total cost of the order both update correctly.</li>
<li>User deletes both tickets for “A Time To Kill” from their basket. This event is completely removed from the cart, leaving only the event “The Casino Killing”.</li>
</ul>

<h3>Checkout</h3>

<ul>
<li>From the Cart page, User clicks “Checkout” and is taken to the checkout page.</li> 
<li>The total cost of the order is correctly displayed at the top of the page. </li>
<li>A form is displyed below allowing the user to input their payment details. User clicks on the button “Submit Payment” without completing every field and receives the message “Please fill in this field”.</li>
<li>User correctly completes the form and clicks “Submit Payment”. User is returned to the “Murder Mysteries” page and receives a message stating “You have successfully paid”.</li>
<li>User enters out of date credit card. User cannot click pay button.</li>
<li>BUG</li>
</ul>

<h3>Screens</h3>

<img src="static/images/laptop.jpg" width="100%">

<h4>Larger Screens</h4>

<p>The banner at the top of the page displays the company name “Stiletto Murder Mysteries” on the left hand side and on the right are shown the company's telephone number and email address, along with the social media links.</p>

<p>The navigation bar displays all of the site’s pages in this view (they are not collapsed).</p>

<p>The modals on the ‘Murder Mysteries” page display the events poster on the right and the event details on the right.</p> 

<h4>Smaller Screens</h4>

<p>The navigation bar is collapsed into a ‘burger’ on smaller screens.</p>
<p>The Telephone number, email address and social media links are hidden. 
<p>Elsewhere, the modals on the ‘Murder Mysteries” page have the poster above the event details.</p>
<p>On the contact page, the form is below the contact details, instead of side by side.</p> 
<p>On the checkout page, the two sections of the payment form are above each other instead of side by side.</p> 
 
<h3>Bugs or problems encountered during testing</h3>


<ul>
<li>If you enter the wrong number of digits in the credit card field this causes an error.</li>
<li>You have successfully logged in! Displays even when they have not. </li>
<li>Reset password doesn't work. </li>
</ul>

<h3>Other Testing</h3>

HTML test to review the code for any errors
Google console to inspect the running of the app for any errors.  


<h2>Deployment</h2>

<p>The project is deployed on <b>Heroku</b>. The code and Readme file are hosted on <b>Github</b>.</p>

<p>The process for deployment on Heroku was:</p>

<ul>
<li>Create a new unique app name in Heroku with “Europe” as the server.</li>
<li>In the workspace, log into Heroku with command Line and the set of commands provided to create a connection between the application and Heroku.</li>
<li>Create a new Git repository and add the files, then associate the Heroku application and push to Heroku once the requirements.txt file and Procfile have been created.</li>
<li>In Heroku, specify the IP and port, so that the server instance will know how to run the application.</li>
<li>IP address is 0.0.0.0</li>
<li>Port is 5000</li>
<li>Open the app to test successful deployment.</li>
</ul>

<p>The process for deployment on Github was:</p>

<ul>
<li>Create new project in Github.</li>
<li>Associate the application with Github, add files and push across using commands provided within Github.</li>
</ul>

<h2>Credits</h2>

<h3>Media</h3>


<p>The images of the creatures are from the following sites:</p>
<ul>
<li><a href="https://www.woodlandtrust.org.uk">www.woodlandtrust.org.uk</a></li>
<li><a href="https://www.rspb.org.uk">www.rspb.org.uk</a></li>
<li><a href="https://www.yorkpress.co.uk">yorkpress.co.uk</a></li>
<li><a href="https://www.nationalgeographic.com">nationalgeographic.com</a></li>
<li><a href="https://www.bbc.co.uk">bbc.co.uk</a></li>
<li><a href="https://www.wikipedia.org">wikipedia.org</a></li>
</ul>


<p>Creature descriptions are from <a href="https://www.wikipedia.org">wikipedia.org</a></p>


<h3>Acknowledgements</h3>

<ul>
<li>Code Institute</li>
<li>Seun Owonikoko</li>
</ul>
