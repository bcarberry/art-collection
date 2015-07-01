from flask import Flask, request, render_template, jsonify, session, redirect
import requests
from sfmoma_api import *

app = Flask(__name__)

@app.route('/')
def index():
	''' Show all artworks with images '''

	print get_artworks()

	return render_template('index.html')


if __name__ == "__main__":
	app.run(port=5000, debug=True)