import os
import flask
import flask_sqlalchemy 
import flask_socketio
import models

app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
socketio = flask_socketio.SocketIO(app)
models.db.init_app(app)

@app.route("/")
def render_home():
	return flask.render_template("home.html")

@app.route("/<string:room_name>", methods=["POST", "GET"])
def render_chat(room_name):
	# get last comment
	return flask.render_template("chat.html", room_name = room_name)


@socketio.on("join")
def join(room_name):
	if(models.Room.query.get(room_name) == None):
		models.Room.create(room_name)
		#create_room(room_name)
	flask_socketio.join_room(room_name)

@socketio.on("request_biggest_id")
def handle_newest_id_request(room_name):
	room = models.Room.query.get(room_name)
	if room == None:
		return "Room with that name doesn't exist!"
	# comments have sequential ID's, thus the latest comment has ID equal to the number of comments
	id = room.num_of_comments

	response={"id" : id, "room_name" : room_name}
	flask_socketio.emit("biggest_id", response, room = flask.request.sid)

@socketio.on("comments_request")
def handle_comments_request(comments_request):
	# requesting comments between the given biggest_id and the given smallest_id
	room_name = comments_request["room_name"]
	biggest_id = comments_request["biggest_id"]
	smallest_id = comments_request["smallest_id"]
	comments = models.Comment.query.filter( \
		models.Comment.room_name == room_name, \
		models.Comment.in_room_id <= biggest_id, \
		models.Comment.in_room_id >= smallest_id \
	)
	jsonified_comments=[c.to_JSON() for c in comments]#list(map(jsonify_comment, comments))
	flask_socketio.emit("update_comment_section", jsonified_comments, room = flask.request.sid)

@socketio.on("new_comment")
def handle_new_comment(comment):
	comment = models.Comment.create(comment)
	flask_socketio.emit("update_comment_section", [comment.to_JSON()], room = comment.room_name)

if __name__ == "__main__":
	port=int(os.environ.get("PORT", 5000)) # For deploying on Heroku
	socketio.run(app, host="0.0.0.0", port=port)
