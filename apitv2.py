import requests
import sys

sw = ['people', 'planets', 'films', 'species', 'vehicles', 'starships']
for i in sw:
    print(i)

def defshow_data(url):
    num = input("Enter the person's ID: ")
    url1 = url + num
    response = requests.get(url1)
    id = response.json()
    print("Name:", id['name'])
    print("Height:", id['height'])
    print("Weight:", id['mass'])
    print("Residence:", id['homeworld'])
    choose_category()

def choose_category():
    url = 'http://swapi.dev/api/'
    c = input("Enter your category here from the options provided: ")
    if c == sw:
        url_data = url + 'people/'
        defshow_data(url_data)
    else:
        print("Please make a different selection")
        choose_category()

choose_category()


