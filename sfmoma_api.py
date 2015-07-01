import requests
import json

def get_artworks():
	''' Get all the artworks with images from the SFMOMA Collection API '''
	f = open('credentials.json').read()
	login = json.loads(f)

	username = login['username']
	password = login['password']

	url = 'http://api.sfmoma.org/collection'
	r = requests.get(url, auth=(username, password)).json()

	return 'success'