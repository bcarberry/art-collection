import requests
import json
import pprint
from models import *
from credentials import *

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


def add_artwork():
	''' Add all the artworks to the database as Art objects '''
	for i in artworks:
		new_artwork = Art(title=i['title'], artist=i['artist'], image=i['image'], artwork_id=i['artwork_id'])
		db.session.add(new_artwork)
    	db.session.commit()
	return 'success'


if __name__ == "__main__":
	save_artworks()
	add_artwork()