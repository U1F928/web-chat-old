# Web Chat

TODO: Screenshots 
![home-page-2-web-chat](https://user-images.githubusercontent.com/110688318/186485755-dfc9c385-1113-4623-a280-c7d730dc6e01.png)

![chat-page-2-web-chat](https://user-images.githubusercontent.com/110688318/186485716-a72e64fe-3e36-4f57-81d9-46eb423af412.png)


Demo web application which allows users to create, join and chat in anonymous chat rooms.

## Live demo

TODO: Link to Heroku

## Description

An in-depth paragraph about your project and overview of use.

* Backend is implemented in Python using the Flask framework. 
* Data is stored in a SQLite database which is integrated via Flask-SQLAlchemy.
* Real-time communication between client and server is handled by Flask-SocketIO.
* Frontend is implemented using vanilla JavaScript, HTML, CSS.

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
Create virtual enviroment in the project directory
```
$ python3 -m venv web-chat/virtual-enviroment
```
Activate the virtual enviroment
```
$ source web-chat/virtual-enviroment/bin/activate
```
Install dependencies into the virtual enviroment
```
(virtual-enviroment) $ python3 -m pip install -r web-chat/requirements.txt
```
Deactivate the virtual enviroment
```
(virtual-enviroment) $ deactivate
```


### Run Locally

Activate the virtual enviroment
```
$ source web-chat/virtual-enviroment/bin/activate
```
Start the server
```
(virtual-enviroment) $ python3 web-chat/src/app.py
```
The web app should now be accessible at `0.0.0.0:5000`

