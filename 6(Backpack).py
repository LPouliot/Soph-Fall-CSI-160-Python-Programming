"""
Author: Lily
Class: CSI-160-01
Assignment: Week 5 Lab
Due Date: 10/13/23

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

import sys

itemsInBackpack = ["book", "computer", "keys", "travel mug"]

while True:
    print("Would you like to:")
    print("1. Add an item to the backpack?")
    print("2. Check if an item is in the backpack?")
    print("3. Quit")
    userChoice = input()

    if (userChoice == "1"):
        print("What item do you want to add to the backpack?")
        itemToAdd = input()
        itemsInBackpack.append(itemToAdd)
        print("You now have", itemsInBackpack)

    if (userChoice == "2"):
        print("What item do you want to check to see if it is in the backpack?: ")
        itemToCheck = input()
        if itemToCheck == itemsInBackpack:
            print("Nope- do you want to add it?")
        else:
            print("Yup! It's all packed and ready to go")

    if (userChoice == "3"):
        sys.exit()

