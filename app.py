from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from credentials import SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/art'
db = SQLAlchemy(app)
app.secret_key = SECRET_KEY


if __name__ == "__main__":
	from views import *
	app.run(port=5000, debug=True)