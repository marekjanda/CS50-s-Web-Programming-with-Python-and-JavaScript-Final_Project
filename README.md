# Final Project

Web Programming with Python and JavaScript

Marek Janda, 17/0/2020

Final project

https://youtu.be/xgI3ZwxxjNw

MODELS
NewsCategory - This class defines categories used as foreign keys in other models. It has two attributes: category_name and category_summary.

Article - This class represents a news article object used in news section of the web site. It has following atrtributes: news_category,
          article_title, published, summary and author, text.

Blog - This class represents a blog object used in blog section of the web site. It has following attributes: category, author, published,
       title, abstract and content.

Project - This class represents a project object in project section of the web site. It has following attributes: owner, category, title,
          published, abstract, description, target_funds, current_funds and attachment. Users can upload a file as attachment to their project
          which will be stored in media folder.

Message - This class represents a message object used to store messages users sent in regards to projects. It has following attributes: 
          project_reference, sender, sent, subject (with choices), message_text and read.

Fund - This class represents a payment, donation, which users can make to support a project. It has following attributes: project_reference,
       donated, contributor, amount.


URLS
Urls with their views and files are as follows.
"" - index.html
The index page is rendered which contains carousel cards with a welcome message, link to register page and short description of content available for registered users. On top of the page is a navbar rendered for not authenticated, logged, users.

"about" - about.html
The 'about' page contains a description of the web site contents.

"register" - register.html
This page contains a registration form. User can register here with their username, first name, last name, email address and password. After they are registered with valid credentials they are logged in and redirected to home page. After authentication the nav bar changes to include content available only for registered users

"login" - login.html
At this page users log in with their username and passowrd. If their credentials are valid they are redirected to home page.

"logout"
By clicking on logout button the user is logged out and redirected to index page.

"home"
When user is authenticated he is redirected to home page which contains cards with short description and link to sections of the web applicationn which are: News, Blogs, Projects. User can navigate to and through these sections via the nav bar.
Images used in this page are from www.freepik.com

"messages" - messages.html
By clicking on messages button on the right side of the nav bar the user can see his messages. Their are devided into two groups: sent and received. Each message in the list is a link to message page where complete message is displayed.

"messages/message/<int:message_id>" - message.html
At this page the user can see a message which he either received or sent regarding a particular project. A Message class object is passed to this page. The user can't reply to the message as messaging not the intent of this web application. Instead the user can see the email address of the sender of the message so he can contact him directly through his email address.

"news" - news.html
At this page cards with abstracts of news articles are displayed. Each card contains the article title, date published, article abstract and a link to article page where the user can read full article. The news section of the web site is available to non-registered users as well. There is an additional navbar so the user can navigate thourgh the news section.

"news/<int:article_id>/article" - article.html
This page contains full article with author and sources. The user can read the full article here. Articles can be written via admin page.

"news/category/<int:category_id>" - news.html
Via the navbar the user can select a category and he is redirected to 'news' page with articles only from the selected category.

"blogs" - blogs.html
Main page of the blog section. The user can see, similar to news page, blogs as cards with each card containing a blog title, author, date published, absrtact and a link to blog page containing a full blog. An additional navbar is displayed to help the user navigate through the blog section.

"blogs/<int:blog_id>/blog" - blog.html
This page contains full blog text with sources.

"blogs/category/<int:category_id>" - blogs.html
Via the navbar the user can select a category and he is redirected to 'blogs' page with blogs only from the selected category.

"blogs/myblogs" - blogs.html
By followng the "My blogs" in the navbar the user can see the blogs page contains just the blogs he or she has written.

"blogs/blogwriting" - blogwriting.html
This page contains a BlogForm from forms.py. The user can write his own blog here. Any registered user can write a blog. Tinymce text editor is used to style the blog content. The text is saved in database as html and when the blog is loaded the browser renders the text so the desired styling is displayed.

"projects" - projects.html
Main page of the project section. This page contains a list of all available projects posted on by the project owners. The project card contains a project title, a date when project was published, the owner of the project, a short summary of the project, target funds the project owner want's to collect and current funds the alredy collected. There is a link to project page as well.

"projects/category/<int:category_id>" - projects.html
ia the navbar the user can select a category and he is redirected to 'projects' page with projects only from the selected category.

"projects/myprojects"
By followng the "My Projects" in the navbar the user can see the projects page contains just the projects he owns and published.

"projects/<int:project_id>/project"
This page contains full project content with title, owner, abstract, date published, target and current funds, an attachment (if available), and full test or description of the project. The attachment uploaded by the owner is available for download. There are two buttons to navigate the user to "support project" page and to "contact owner" page.

"projects/start_project" - startproject.html
This page contains a form where the user can start and publish his own project to request funds or collaboration and help or simpy to advertise his project. The form data are stored in Project object described above. The user can upload an attachment which is stored in media folder. The media folder has structured as follows: 'media/uploads/Year/Month/Day/'.

"projects/<int:project_id>/support_project" - fundproject.html
At this page there is a cart payment form from 'stripe'. The user can type in the amount his card details and a payment will be submitted via stripe (only dummy card possible as real payment is disabled for safety purposes). Card credential are checked by JavaScript code using stripe.js library. Ater form is submitted and card number verified the 'current_funds' attribute of the particular project object is incremented by the amount and payment object is created in database. When the owner visits the project site he can see all the contributions to his project with date, amount and user who supported his project.

"projects/<int:project_id>/contact_owner" - contactpage.html
At this page the user can contact the owner of the project. He can select a subject of his message and write a text of the message into the text field. Following subjects are available: More information, Collaboration offer, Join project, Make investment, Advertisement and Other business offer. After sending the message a message object is created and the recipient (project owner) can see the message on his messages page.

STATIC FILES
CSS fodler
This folder contains two files: stripe.css and styles.css. "stripe.css" contains styling for the payment form of stripe. "styles.css" cotains styling of every other page of the application.

Images folder
This folder contains all the images used in the web applications. The source of the images is www.freepik.com

JS folder
This folder contains jquery-3.4.1.js file with jquery library.