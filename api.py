import requests
import sys

sw = ['people', 'planets', 'films', 'species', 'vehicles', 'starships']
url = 'http://swapi.dev/api/' # type in this url into google to find the api root
response = requests.get(url) # make a request to this website and get everything in the root directory, all the data
                             # Stored all in the response variable
show_stuff = response.json() # Just lists[] and doctrinaires{} for json
print(show_stuff)
