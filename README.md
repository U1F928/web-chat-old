# Web Chat

TODO: Screenshots 

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
$ git clone https://github.com/U1F928/chatRoom
```
Create virtual enviroment in the project directory
```
$ python3 -m venv chatRoom/virtual_enviroment
```
Activate the virtual enviroment
```
$ source chatRoom/virtual_enviroment/bin/activate
```
Install dependencies into the virtual enviroment
```
$ python3 -m pip install -r chatRoom/requirements.txt
```
Deactivate the virtual enviroment
```
$ deactivate
```


### Run Locally

Activate the virtual enviroment
```
$ source chatRoom/virtual_enviroment/bin/activate
```
Start the server
```
$ python3 chatRoom/src/app.py
```
The web app should be accessible at `0.0.0.0:5000`

