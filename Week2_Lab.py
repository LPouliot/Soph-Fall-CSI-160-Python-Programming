"""
Author: Lily Pouliot
Class: CSI-160-01: Python Programming
Assignment: Week 2: Lab - Conversation with a Computer
Due Date: 9/15/23

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

print("Hello and Welcome to my Survey!")

name = input("Please enter your name here:")
print("Hello", name ,"I have some questions for you today.")
# This was used to get their name, the variable is called name

length = len(name)
print("But just so you know, the number of characters in your name is,",length)
# This was used to the length of the name using the input from the last variable

color = input("What is your favorite color:")
print(color,"?","Hmm very interesting", name ,"...")
color2 = input("Does your family like the color " + color + ":")
print(color2,"?","Okay, let's move on.")
# The two variables above ask about the person's favorite color and if their family likes the same color

animal = input("Please list your favorite mythical animal:")
print("Okay let's see what you put down-", animal ,"-Very cool!")
print("Surprisingly, a favorite mythical animal can say a lot about a person.")
# This is asking about the favorite mythical animal and saying that they made a good choice

sib = int(input("How many siblings do you have:"))
one = 1
sum = sib + one
print("Very nice, you are one of the", sum ,"kids in your family.")
# This helps converts the number of kids with the one person taking the survey
# int converts it into an integer so the number works

print("Almost there! You have one question left.")
print(name,"You are one of our 5 precipitants today!")
people = 5
p1 = 7.75
p2 = 8.01
p3 = 6.58
p4 = 5.23
p5 = float(input("Out of 1.00 to 10.00, how did you think you did:"))
gsum = (p1 + p2 + p3 + p4 + p5)
avg = gsum / people
print("Compared to our other results, you scored:", avg, "!")
avg1 = gsum // people
print("That is", avg1 ,"Rounded to the nearest whole number.")
print("Congrats and thank you for taking the survey!")
fun = input("Did you enjoy the survey?")
print("Perfect, your answer has been recorded. Have a great day!")
# I created a system that compares the user's grade to the others
# The float was used for the decimal points since the integer cannot
# I used // to round the divided number














