# Web Chat 
 
A simple web application that allows users to create, join and chat in anonymous chat rooms. 
 
## Live Demo 
 
https://web-chat.fly.dev/ 
 
## Built With
 
* Backend is implemented in **Python** using the **Flask** framework. 
* Data is stored using a **SQLite** database engine and **SQLAlchemy**
* Real-time communication between client and server is handled by **Socket.IO**. 
* Frontend is implemented using **JavaScript**, **HTML**, **CSS**. 
 
## Getting Started 
 
### Prerequisites 
 
* python3 
* python3-pip 
* python3-venv 
* git 
 
### Installation 
 
Clone the project 
``` 
$ git clone https://github.com/U1F928/web-chat 
``` 
Create a virtual environment in the project directory 
``` 
$ python3 -m venv web-chat/virtual_environment 
``` 
Activate the virtual environment 
``` 
$ source web-chat/virtual_environment/bin/activate 
``` 
Install dependencies into the virtual environment 
``` 
(virtual_environment) $ python3 -m pip install -r web-chat/requirements.txt 
``` 
Deactivate the virtual environment 
``` 
(virtual_environment) $ deactivate 
``` 
 
 
### Run Locally 
 
Activate the virtual environment 
``` 
$ source web-chat/virtual_environment/bin/activate 
``` 
Start the server 
``` 
(virtual_environment) $ python3 web-chat/run.py 
``` 
The web app should now be accessible at `0.0.0.0:5000` 
 
## Screenshots 
 
![home-page-3-web-chat](https://user-images.githubusercontent.com/110688318/186491454-38f28670-9f62-41c1-9495-ec39c5f35693.png) 
 
 
![chat-page-2-web-chat](https://user-images.githubusercontent.com/110688318/186485716-a72e64fe-3e36-4f57-81d9-46eb423af412.png)
