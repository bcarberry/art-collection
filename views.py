from flask import render_template, request, session
from models import *
from app import app


@app.route('/')
def index():
	''' Show all artworks with images '''
	art = Art.query.all()

	return render_template('index.html', art=art)