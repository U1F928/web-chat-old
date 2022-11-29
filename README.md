# Web Chat 
 
A simple web application that allows users to create, join and chat in anonymous chat rooms. 
 
## Live Demo 
 
https://web-chat.fly.dev/ 
 
## Built With
 
* Back end is implemented in **Python** using the **Flask** framework. 
* Data is stored using an **SQLite** database engine and **SQLAlchemy**.
* Real-time communication between the client and the server is handled by **Socket.IO**. 
* Front end is implemented using **JavaScript**, **HTML**, and **CSS**. 
 
## Getting Started 
 
### Prerequisites 
 
* Docker
* Git
 
### Installation 
 
Clone the project 
``` 
$ git clone https://github.com/U1F928/web-chat 
``` 
Build the image
``` 
$ docker build -t web-chat-image web-chat
``` 
 
 
### Run Locally 
 

``` 
$ docker run --detach --publish 0.0.0.0:80:8080 web-chat-image
``` 
The web application should now be accessible at `0.0.0.0` 
 
## Screenshots 
 
![web-chat-home](https://user-images.githubusercontent.com/110688318/189998833-dfbafa5c-eb1b-4c1f-b1fa-fe9d5bca44e8.png)

![web-chat-chat](https://user-images.githubusercontent.com/110688318/189998850-a4dc68ee-74f2-484e-b601-03b2ad3ab1b3.png)


