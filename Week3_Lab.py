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
# First Function: Adding numbers together
# Second Function: "Login" with names
# Third Function: Feet to Meters (Trying to give myself a challenge)

def calc():
    '''
    In this def, z and y are being added together and returned in the x variable
    The result of the operation is held in memory, the function call results in the answer of becoming available
    The return value is x
    '''
    z = 45
    y = 235
    x = z + y
    return x
calc()
print(calc())


def MultiQuestions():
    """
    In this function, the user is placing their name and level in python and the function is checking it
    The else if statement is to make sure the user is putting in their information
    The assumptions are that the user knows this information needed, like their name and numbers
    """
    name = input("Enter Your name:")
    print("Enter either 1, 2, 3, 4, or 5")
    pyth = input("What is your skill level for Python:")
    if (name == "" or pyth == ""):
        print("You need to enter your information")
    else:
        print("Thank you")

MultiQuestions()


def FeetToMeters(feet):
    """
    This function takes a number  from the user and then uses division to convert into a meter
    The argument inside the function is called feet since it used to store the input feet number
    The return value is meter, as it takes the converted feet to meter and outputs the result
    Assumptions are that the computer knows how to change numbers to binary and that the user knows how the value of feet
    """
    meter = round(feet / 3.281) # Divide the number by the meters
    # I found the round function so the meter number is smaller
    return meter

print("Your number will be converted into meters")
feet = float(input("Please enter a number of feet:")) # Converted the numbers into string in order for them to work
meters = FeetToMeters(feet)
print( str(feet) + " Feet is converted to " + str(meters) + " meters ")






