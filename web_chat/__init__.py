import os
import flask
import web_chat.views
import web_chat.models
import web_chat.sockets

app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.add_url_rule("/", view_func=web_chat.views.render_home)
app.add_url_rule("/<string:room_name>", view_func=web_chat.views.render_chat)

web_chat.models.db.init_app(app)
web_chat.sockets.socketio.init_app(app)

with app.app_context():
    web_chat.models.db.create_all()  # create tables if they don't exist
