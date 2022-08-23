import os
import flask
import views
import models
import sockets

app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.add_url_rule("/", view_func=views.render_home)
app.add_url_rule("/<string:room_name>", view_func=views.render_chat)

models.db.init_app(app)
sockets.socketio.init_app(app)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # For deploying on Heroku
    sockets.socketio.run(app, host="0.0.0.0", port=port)
