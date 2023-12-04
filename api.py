import requests
import sys

sw = ['people', 'planets', 'films', 'species', 'vehicles', 'starships']
for i in sw:
    print(i)

def defshow_people(url):
    num = input("Enter the person's ID: ")
    url1 = url + num
    response = requests.get(url1)
    id1 = response.json()
    print("Name:", id1['name'])
    print("Height:", id1['height'])
    print("Weight:", id1['mass'])
    print("Residence:", id1['homeworld'])
    choose_category()

def defshow_planets(url):
    num2 = input("Enter the planet's ID ")
    url2 = url + num2
    response = requests.get(url2)
    id2 = response.json()
    print("Name:", id2['name'])
    print("Diameter:", id2['diameter'])
    print("Rotation:", id2['rotation_period'])
    print("Climate:", id2['climate'])
    print("Terrain:", id2['terrain'])
    print("Population:", id2['population'])
    choose_category()

def defshow_films(url):
    num3 = input("Enter the film's ID: ")
    url3 = url + num3
    response = requests.get(url3)
    id3 = response.json()
    print("Title:", id3['title'])
    print("Episode:", id3['episode_id'])
    print("Release Date:", id3['release_date'])
    print("Setting:", id3['opening_crawl'])
    choose_category()

def choose_category():
    url = 'http://swapi.dev/api/'
    c = input("Enter your category here from the options provided: ")
    if c == 'people':
        url_people = url + 'people/'
        show_people = url_people
        defshow_people(show_people)

    elif c == "planets":
        url_planets = url + "planets/"
        show_planets = url_planets
        defshow_planets(show_planets)

    elif c == "films":
        url_films = url + "films/"
        show_films = url_films
        defshow_films(show_films)

    else:
        print("Process under construction")
        print("Please make a different selection")
        choose_category()

choose_category()
