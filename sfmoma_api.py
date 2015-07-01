import requests

def get_artworks():
	''' Get all the artworks with images from the SFMOMA Collection API '''

	username = 'sfmoma01'
	password = 'art+data'
	url = 'http://api.sfmoma.org/collection'
	headers = { 'username': username, 'password': password } 

    r = requests.get(url, headers=headers).json()

    print r
    return r