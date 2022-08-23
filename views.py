import flask


def render_home():
    return flask.render_template("home.html")


def render_chat(room_name):
    # get last comment
    return flask.render_template("chat.html", room_name=room_name)
