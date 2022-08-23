import flask_socketio
import flask
import models
socketio = flask_socketio.SocketIO()

@socketio.on("join")
def join(room_name):
    if models.Room.query.get(room_name) == None:
        models.Room.create(room_name)
        # create_room(room_name)
    flask_socketio.join_room(room_name)


@socketio.on("request_biggest_id")
def handle_newest_id_request(room_name):
    room = models.Room.query.get(room_name)
    if room == None:
        return "Room with that name doesn't exist!"
    # comments have sequential ID's, thus the latest comment has ID equal to the number of comments
    id = room.num_of_comments

    response = {"id": id, "room_name": room_name}
    flask_socketio.emit("biggest_id", response, room=flask.request.sid)


@socketio.on("comments_request")
def handle_comments_request(comments_request):
    # requesting comments between the given biggest_id and the given smallest_id
    room_name = comments_request["room_name"]
    biggest_id = comments_request["biggest_id"]
    smallest_id = comments_request["smallest_id"]
    comments = models.Comment.query.filter(
        models.Comment.room_name == room_name,
        models.Comment.in_room_id <= biggest_id,
        models.Comment.in_room_id >= smallest_id,
    )
    # list(map(jsonify_comment, comments))
    jsonified_comments = [c.to_JSON() for c in comments]
    flask_socketio.emit(
        "update_comment_section", jsonified_comments, room=flask.request.sid
    )


@socketio.on("new_comment")
def handle_new_comment(comment):
    comment = models.Comment.create(comment)
    flask_socketio.emit(
        "update_comment_section", [comment.to_JSON()], room=comment.room_name
    )


