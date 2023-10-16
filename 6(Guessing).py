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

from random import randint
randomNum = randint(1,100)

guess = 0 # A guess needs to be addressed outside of the while loop to avoid loop hell

while guess != randomNum:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > randomNum:
        print("Too High! Try Again!")
    elif guess < randomNum:
        print("Too Low! Try Again!")
    else:
        print("You did it! You found the right number!")
