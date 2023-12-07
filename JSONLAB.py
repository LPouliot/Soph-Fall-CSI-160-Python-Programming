"""
Author: Lily
Class: CSI-160-01
Assignment: Week 10/11 Lab
Due Date: 11/30/23

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
'''
I will be using the DND framework.
And creating a NPC randomizer out of the nested files inside the main root
'''

import requests
import random

print("Here is your randomized NPC for D&D:")

"""
This function below grabs all of the DND class names, puts them into a list, and randomizes it 
"""
def grab_classes():
    response = requests.get('https://api.open5e.com/v1/classes/') # A specific classes section found in the root API
    names = response.json()
    classes = names["results"]
    class_list = [] # creating a list to store the names
    for c in classes:
            class_list.append(c["name"])

    random_class = random.choice(class_list)  # Found out this is how to randomize the list through W3school
    print("NPC Class:", random_class) # Output the randomly selected class

grab_classes()


"""
This function below grabs all of the DND races, puts them into a list, and randomizes it 
"""
def grab_races():
    response = requests.get('https://api.open5e.com/v1/races/') # A specific classes section found in the root API
    names = response.json()
    races = names["results"]
    race_list = [] # creating a list to store the names
    for c in races:
            race_list.append(c["name"])

    random_race = random.choice(race_list)  # Found out this is how to randomize the list through W3school
    print("NPC Race:", random_race) # Output the randomly selected class

grab_races()

"""
This function below grabs all of the DND weapons, puts them into a list, and randomizes it 
"""
def grab_weapons():
    response = requests.get('https://api.open5e.com/v1/weapons/') # A specific classes section found in the root API
    names = response.json()
    weapons = names["results"]
    weapon_list = [] # creating a list to store the names
    for c in weapons:
            weapon_list.append(c["name"])

    random_weapons = random.choice(weapon_list)  # Found out this is how to randomize the list through W3school
    print("NPC Weapon:", random_weapons) # Output the randomly selected class

grab_weapons()


"""
This function below grabs all of the DND armor, puts them into a list, and randomizes it 
"""
def grab_armor():
    response = requests.get('https://api.open5e.com/v1/armor/') # A specific classes section found in the root API
    names = response.json()
    armor = names["results"]
    armor_list = [] # creating a list to store the names
    for c in armor:
            armor_list.append(c["name"])

    random_armor = random.choice(armor_list)  # Found out this is how to randomize the list through W3school
    print("NPC Armor:", random_armor) # Output the randomly selected class

grab_armor()


"""
This function below grabs all of the DND spells, puts them into a list, and randomizes it 
"""
def grab_spells():
    response = requests.get('https://api.open5e.com/v1/spells/') # A specific classes section found in the root API
    names = response.json()
    spells = names["results"]
    spells_list = [] # creating a list to store the names
    for c in spells:
            spells_list.append(c["name"])

    random_spells = random.choice(spells_list)  # Found out this is how to randomize the list through W3school
    print("NPC Spell:", random_spells) # Output the randomly selected class

grab_spells()


"""
This function below grabs all of the DND backgrounds, puts them into a list, and randomizes it 
"""
def grab_spells():
    response = requests.get('https://api.open5e.com/v1/backgrounds/') # A specific classes section found in the root API
    names = response.json()
    background = names["results"]
    background_list = [] # creating a list to store the names
    for c in background:
            background_list.append(c["desc"])

    random_background = random.choice(background_list)  # Found out this is how to randomize the list through W3school
    print("NPC Background:", random_background) # Output the randomly selected class

grab_spells()