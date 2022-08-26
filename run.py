import os
import web_chat

if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 5000
    print(f"Running on {HOST}:{PORT}")
    # Using an embedded server with eventlet
    # https://flask-socketio.readthedocs.io/en/latest/deployment.html
    web_chat.sockets.socketio.run(web_chat.app, host=HOST, port=PORT)
