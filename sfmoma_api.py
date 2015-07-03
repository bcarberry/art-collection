import requests
import json
import pprint
from models import *

# Get API credentials from local file
f = open('credentials.json').read()
login = json.loads(f)
username = login['username']
password = login['password']

# Artworks will be saved to a list of dictionaries
artworks = []

def get_artworks():
	""" Get artworks with images out of the API """

	url = 'https://api.sfmoma.org/collection/artworks?per_page=500'
	r = requests.get(url, auth=(username, password)).json()

	return r

def save_artworks():
	""" Save artworks with an image to a dictionary """
	r = get_artworks()

	for i in r:
		if i['image']['image_url'] is not None:
			artwork = {}
			artwork['artwork_id'] = i['artwork_id']
			artwork['title'] = i['display_title']
			artwork['image'] = i['image']['image_url']

			for i in i['creators']:
				a = []
				a.append(i['artist'])
				artists = ''
				artists = ', '.join(a)

			artwork['artist'] = artists
			artworks.append(artwork)

	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(artworks)
	print len(artworks)
	return artworks


# Add the artworks to the database
def add_artwork():
	for i in artworks:
		new_artwork = Artwork(title=i['title'],)




if __name__ == "__main__":
	save_artworks()