import json
import sys
import urllib.parse
import requests

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

while (True):
	address = '92620' #input('Address')
	if address =='q' or address == 'quit':
		break
	url = main_api + urllib.parse.urlencode({'address':address})
	jsaon_data = requests.get(url).json()
	
	if jsaon_data['status'] == 'OK':
		print(jsaon_data['results'][0]['formatted_address'])
		for each in jsaon_data['results'][0]['address_components']: 
			print(each['long_name'])
