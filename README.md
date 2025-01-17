Django Chat Application-

This is a simple Django-based chat application that allows users to register, log in, and chat with each other. The application includes basic functionalities like viewing a list of users, starting a chat with a user, sending and receiving messages, and viewing chat history.

Features-

User registration and login functionality
View a list of users to start chatting with
Real-time chat messages between users
Display of message history between users
Basic frontend with a sidebar for navigation
Technologies Used
Django 5.1.5 (Backend)
SQLite (Database)
HTML/CSS (Frontend)
Python 3.x

Installation-

Follow these steps to get the project up and running on your local machine.

1. Clone the repository

git clone https://github.com/sparshspradhan/chat-app-xy.git
cd chat-app
2. Set up a virtual environment
It’s a good practice to create a virtual environment for your project.


python3 -m venv venv
source venv/bin/activate   # For Windows use: venv\Scripts\activate

3. Install dependencies
Make sure you have the required Python packages installed.


pip install -r requirements.txt

4. Run migrations
Set up the database and apply migrations.


python manage.py migrate

5. Create a superuser (Optional)
You can create a superuser to access the Django admin interface.


python manage.py createsuperuser

6. Run the development server
Start the Django development server.



python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

Usage-

Register a new user: Visit /register/ to create a new account.
Login: Visit /login/ to log in to your account.
Start a chat: After logging in, you can view the list of other users and start chatting with them.
Send messages: Type a message in the text box and click "Send" to send it.
View message history: Messages exchanged between users are displayed in the chat room.

Folder Structure-


chat_app/
├── chat/
│   ├── migrations/
│   ├── templates/
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── chat.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── consumers.py
│   ├── models.py
│   ├── routing.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── chat_app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py


           
Contributing
Feel free to fork the repository, make changes, and submit pull requests. If you find any issues or have suggestions, please open an issue in the repository.


