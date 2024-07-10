# CHATS : Real-Time Messaging Web Application

## Introduction:
**CHATS** is a real-time messaging web application similar to WhatsApp Web, where users can send and recieve messages in real-time with their contacts.

## Technologies Used:

- HTML
- CSS
- Javascript
- Django

## Installation:
1. Download the code in a zip file from the repository:
https://github.com/me50/joelwilliam2005/tree/web50/projects/2020/x/capstone

2. Next, 'cd' into the folder.
   ```bash
   cd joelwilliam2005-web50-projects-2020-x-capstone/ 

3. Run following commands in the terminal in the same directory:

	```bash
	python manage.py makemigrations chats
	python manage.py migrate
	python manage.py createsuperuser
    
> **Note:** 
Use only the username mentioned below for the 'createsuperuser' command, it is required for the function that lists all the users on the chats app. Email is optional and any password can be chosen.
		- Username: **chats_admin_user**
		-	Email address: {OPTIONAL}
		-	Password: {ANY}
4. Finally start the server:

	```bash
	python manage.py runserver

5. The runserver command should now run the web app and should be available to access through a web browser from http://127.0.0.1:8000/ .

## Usage:
1. Upon accessing 'http://127.0.0.1:8000/' you would be redirected to the login and register page.

2. Register into the CHATS app by filling the following details:
	- First Name
	- Last Name
	- Username
	- Password

3. Upon registering, you will be redirected to the CHATS app landing page. 
> **Note:**
By default the ' My contacts ' and ' Find People ' options would not be accessible because there are no other users in the database.
Open a private window or a new tab in another browser and register another new user into the CHATS app. 
You can use this window in a Mobile view to try the responsive nature of the CHATS app. **Reload the web app once when trying the mobile view.**

4. The ' Find People ' will now become accessible and clicking this should list all the users that are registered on the website.

5. The 'ADD' button beside the user can be used to add the respective user to your contacts.

6. The ' My Contacts ' option should now be accessible, and clicking it should list all the users that are in your contacts.

7. Clicking on the user you added in your contacts showed in ' My Contacts ' listing should now bring up Chat box.

8. You can now type messages in the text input area and send it using the send button.

9. You can start messaging any user even if that user has not added you in their contact. Sending a message would automatically add you in their contact list.

 10.  All the sent and recieved messages should immediately show up in the message box, as the message box is updated/refreshed every second.

## File Structure: 

- `capstone/`
  - `__pycache__/`
  - `__init__.py`
  - `asgi.py`
  - `settings.py`
  - `urls.py`
  - `wsgi.py`
- `chats/`
  - `__pycache__/`
  - `migrations/`
  - `static/`
    - `chats/`
      - `fonts/` 
        - `Ubuntu-Regular.ttf`
      - `index.css`
      - `index.js`
      - `login_and_register.css`
      - `login_and_register.js`
      - `style.css`
  - `templates/`
    - `chats/`
      - `index.html`
      - `layout.html`
      - `login_and_register.html`
  - `__init__.py`
  - `admin.py`
  - `apps.py`
  - `models.py`
  - `tests.py`
  - `urls.py`
  - `views.py`
- `manage.py`
- `README.md`
- `db.sqlite3`

1. The root folder contains the capstone (django-project) folder and the chats (django_app) folder.
2. The fonts folder in the static folder contains the font used for the styling of the project.
3. The files 'login_and_register.css' and 'login_and_register.js'  in the static folder contains CSS and Javascript for the login and register page styling and functionality respectively.
4. The files 'index.css' and 'index.js'  in the static folder contains CSS and Javascript for the CHATS app landing page that contains all styling and functionality of features like hover animation, button click feedback, messaging, adding contacts, updating message box, etc.
5. The templates folder contains the HTML files for the CHATS app that are based/extended on a single 'layout.html' file. These contain the HTML elements for the login and register page and CHATS app landing page.
6. The 'admin.py' file in the 'chats/' directory contains the registeration of the models to show up in the admin page.
7. The 'models.py' file in the 'chats/' directory contains all the models that are further converted into database tables by django's inbuilt ORM.
8. The 'urls.py' file in the 'chats/' directory contains all the urls associated with the project to access different pages and call APIs.
9. The 'views.py' file in the 'chats/' directory contains all the functions that provide the features like sending all messages and user from backend to frontend.

## Distinctiveness and Complexity 

This project stands out because of its unique feature that allows real-time messaging that is the **Continously Updating Message Box** this allows the messages to show up immediately after sending or recieving the message.

This project also differs from the previous projects listed in CS50w course because of its **Mobile Responsive Design**.
When the web app senses that the width and height of the screen resembles a mobile phone it changes its design by completely hiding the chat box. It shows the home page that shows my contacts and on clicking the contact the homepage  is replaced by the chatbox. The user can also go back to the homepage using the back button that shows up beside the contact username in the chatbox that only shows up in mobile view.

All the features of the **CHATS** app work on a single page without reloading the URL, hence it is a complete single page web app, excluding the login and register functionality.

The HTML, CSS and Javascript files of the project are separated into various different files according to their function to ensure better understanding of the code base, where the CSS in the project totals upto nearly 400 lines of code, the javascript totals upto nearly 500 lines of code.

By this it can be concluded that the design and complexity of of this project exceed those of the previously made projects listed in CS50W course, and the project is distinct and unique from the other projects in the course.
