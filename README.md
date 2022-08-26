# Web Chat

Simple web application which allows users to create, join and chat in anonymous chat rooms.

## Live Demo

https://web-chat.fly.dev/

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
(virtual-enviroment) $ python3 web-chat/run.py
```
The web app should now be accessible at `0.0.0.0:5000`

## Screenshots

![home-page-3-web-chat](https://user-images.githubusercontent.com/110688318/186491454-38f28670-9f62-41c1-9495-ec39c5f35693.png)


![chat-page-2-web-chat](https://user-images.githubusercontent.com/110688318/186485716-a72e64fe-3e36-4f57-81d9-46eb423af412.png)
