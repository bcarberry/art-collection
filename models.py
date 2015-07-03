from app import db

# Create a table for many-to-many hearts relationships
hearts = db.Table('hearts',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
	db.Column('art_id', db.Integer, db.ForeignKey('artwork.id'))
)

# Create a database table for Artworks
class Artwork(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(250))
	artist = db.Column(db.String(250))
	image = db.Column(db.String(250))
	artwork_id = db.Column(db.Integer)
	hearts = db.relationship('Heart', secondary=hearts, 
		backref=db.backref('hearts', lazy='dynamic'))

	def __init__(self, title, artist, image, artwork_id):
		self.title = title
		self.artist = artist
		self.image = image
		self.artwork_id = artwork_id

# Create a model for Hearts
class Heart(db.Model):
	id = db.Column(db.Integer, primary_key=True)


# Create a database table for Users
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(250))
	name = db.Column(db.String(250))
	avatar = db.Column(db.String(250))
	hearts = db.relationship('Heart', secondary=hearts, 
		backref=db.backref('hearts', lazy='dynamic'))

	def __init__(self, username, name, avatar):
		self.username = username
		self.name = name
		self.avatar = avatar




if __name__ == '__main__':
	print 'Creating database tables...'
	db.create_all()
	print 'Done!'