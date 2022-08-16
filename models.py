import flask 
import flask_sqlalchemy 

db = flask_sqlalchemy.SQLAlchemy()

class Room(db.Model):
	name = db.Column(db.String(30), primary_key=True)
	num_of_comments = db.Column(db.Integer)
	comments = db.relationship("Comment")
	
	@staticmethod
	def create(room_name):
		new_room = Room(name = room_name, num_of_comments = 0)
		db.session.add(new_room)
		db.session.commit()

class Comment(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	text = db.Column(db.String(800), unique = False, nullable = False)
	room_name = db.Column(db.String(30), db.ForeignKey("room.name"))
	in_room_id = db.Column(db.Integer, index = True)

	@staticmethod
	def create(comment):
		room_name = comment["room_name"]
		text = comment["text"]
		room = Room.query.get(room_name)
		room.num_of_comments += 1
	
		new_comment = Comment(
			text = text, room_name = room_name, in_room_id = room.num_of_comments
		)
		db.session.add(new_comment)
		db.session.commit()
		return new_comment

	def to_JSON(self):
		json={"room_name" : self.room_name, "in_room_id" : self.in_room_id, "text" : self.text}
		return json
