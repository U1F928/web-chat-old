import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from engineio.payload import Payload

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
socketio = SocketIO(app)
db = SQLAlchemy(app)


class Room(db.Model):
    name = db.Column(db.String(30), primary_key=True)
    num_of_comments = db.Column(db.Integer)
    comments = db.relationship("Comment")

def create_room(room_name):
    new_room=Room(name=room_name, num_of_comments=0)
    db.session.add(new_room)
    db.session.commit()

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(800), unique=False, nullable=False)
    room_name = db.Column(db.String(30), db.ForeignKey("room.name"))
    in_room_id = db.Column(db.Integer, index=True)

def add_comment_to_DB(comment):
    room_name = comment["room_name"]
    text = comment["text"]
    room = Room.query.get(room_name)
    room.num_of_comments += 1

    new_comment = Comment(
        text=text, room_name=room_name, in_room_id=room.num_of_comments
    )
    db.session.add(new_comment)
    db.session.commit()
    return new_comment

def jsonify_comment(comment):
    json={"room_name":comment.room_name, "in_room_id":comment.in_room_id, "text":comment.text}
    return json

@app.route("/")
def render_home():
    return render_template("home.html")

@app.route("/<string:room_name>", methods=["POST", "GET"])
def render_chat(room_name):
    # get last comment
    return render_template("chat.html", room_name=room_name)


@socketio.on("join")
def join(room_name):
    if(Room.query.get(room_name)==None):
        create_room(room_name)
    join_room(room_name)

@socketio.on("request_biggest_id")
def handle_newest_id_request(room_name):
    id=Room.query.get(room_name).num_of_comments
    response={"id": id, "room_name": room_name}
    emit("biggest_id", response, room=request.sid)

@socketio.on("comments_request")
def handle_comments_request(comments_request):
    # requesting comments between given biggest_id and given smallest_id
    room_name=comments_request["room_name"]
    biggest_id=comments_request["biggest_id"]
    smallest_id=comments_request["smallest_id"]
    comments=Comment.query.filter(Comment.room_name==room_name, Comment.in_room_id<=biggest_id, Comment.in_room_id>=smallest_id)
    jsonified_comments=list(map(jsonify_comment, comments))
    emit("update_comment_section", jsonified_comments, room=request.sid)

@socketio.on("new_comment")
def handle_new_comment(comment):
    comment=add_comment_to_DB(comment)
    emit("update_comment_section", [jsonify_comment(comment)], room=comment.room_name)

if __name__ == "__main__":
    port=int(os.environ.get("PORT", 5000)) # For deploying on Heroku
    socketio.run(app, host="0.0.0.0", port=port)
