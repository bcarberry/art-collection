from flask import Flask, request, render_template, jsonify, session, redirect
import requests
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/art'
db = SQLAlchemy(app)

@app.route('/')
def index():
	''' Show all artworks with images '''

	return render_template('index.html')


if __name__ == "__main__":
	app.run(port=5000, debug=True)