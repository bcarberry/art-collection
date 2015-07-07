from flask import render_template, request, session, redirect, url_for
from models import *
from app import app
from credentials import CLIENT_ID, CLIENT_SECRET
import requests

@app.route('/')
def index():
	''' Show all artworks with images '''
	art = Art.query.all()

	return render_template('index.html', art=art)


@app.route('/login')
def login():
	''' Use Google OAUTH to log the user in '''
	signin_url = 'https://accounts.google.com/o/oauth2/auth?'
 
	parameters = ['client_id={}'.format(CLIENT_ID),
		'redirect_uri={}'.format('http://localhost:5000/oauth2callback'),
		'response_type=code',
		'scope=profile']
 
	signin_url += '&'.join(parameters)
 
	return redirect(signin_url)

@app.route('/oauth2callback')
def callback():
	code = request.args.get('code')
	error = request.args.get('error')
	if error:
	    return("Error! {}".format(error))

	# Exchange the code for an access token
	token_url = 'https://accounts.google.com/o/oauth2/token'
	data = {
	    'client_id': CLIENT_ID,
	    'client_secret': CLIENT_SECRET,
	    'redirect_uri': 'http://localhost:5000/oauth2callback',
	    'code': code,
	    'grant_type': 'authorization_code'
	}

	r = requests.post(token_url, data=data)

	# In an ideal world we would store this token and use it to make all our
	# future API requests.
	token = r.json().get('access_token')

	# Now we're going to call a Google API, in this case the userinfo API
	r = requests.get('https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={}'.format(token))

	session['user'] = r.json()
	print session['user']

	return redirect('/my-art')

@app.route('/my-art')
def my_art():
	''' Logged in user account page '''
	user = session['user']
	
	return render_template('my_art.html', user=user)
