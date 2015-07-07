from app import app, db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Create a table for many-to-many hearts relationships
hearts = db.Table('hearts',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
	db.Column('art_id', db.Integer, db.ForeignKey('art.id'))
)

# Create a database table for Artworks
class Art(db.Model):
	__tablename__ = 'art'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(250))
	artist = db.Column(db.String(250))
	image = db.Column(db.String(250))
	artwork_id = db.Column(db.Integer)
	hearts = db.relationship('User', secondary=hearts)

	def __init__(self, title, artist, image, artwork_id):
		self.title = title
		self.artist = artist
		self.image = image
		self.artwork_id = artwork_id


# Create a database table for Users
class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(250))
	name = db.Column(db.String(250))
	avatar = db.Column(db.String(250))
	hearts = db.relationship('Art', secondary=hearts)

	def __init__(self, username, name, avatar):
		self.username = username
		self.name = name
		self.avatar = avatar


# Create a model for Hearts
# class Heart(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)


if __name__ == '__main__':
	manager.run()