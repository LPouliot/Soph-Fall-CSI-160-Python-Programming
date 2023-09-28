"""This file can convert binary, hexadecimal, and base-10 integer inputs into each other.

Authors: Adra Gonzalez, Savannah Ciak, Hannelore Sanokklis, Lily Pouliot
Class: CSI-160-01
Assignment: Class Exercise 1
Due Date: 21 September 2023

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


def start_conversion():
    """ This function asks the user what conversion they would like to do between binary,
    hexadecimal, and base-10 integer numbers.

    Returns:
        The conversion value, which will be done in separate functions below. This function contains print values,
        and the return statements are pulled from the functions below.

    Assumptions:
        The user knows the difference between hexadecimal, binary, and base-10 values
        The user knows what an integer is
        The user inputs an integer value as a choice
        The user inputs the proper binary, hexadecimal, or base-10 type value for the conversion they choose

    """
    print('''You have the options to convert:
    Binary to Hexadecimal (1)
    Binary to Base-10 (2) 
    Hexadecimal to Base-10 (3)
    Hexadecimal to Binary (4)
    Base-10 to Binary (5)
    Base-10 to Hexadecimal (6)''')  # A comment block was used to improve formatting

    conversion_type = int(input("What conversion do you want? Please enter an integer number between 1-6. Reference the options above."))

    if conversion_type == 1:
        num = int(input("What is the binary number?"), 2)  # In int(x, 2) the 2 is used to show
        # that the input is a base 2 (binary) number. We found this in the class modules.
        print("The hexadecimal number is:", bin_to_hex(num))

    elif conversion_type == 2:
        num2 = int(input("What is the binary number?"), 2)
        print("The base-10 integer number is:", bin_to_base10(num2))

    elif conversion_type == 3:
        num3 = int(input("What is the Hexadecimal number?"), 16)  # In int(x, 16) the 16 is used to show
        # that the input is a hexadecimal number
        print("The base-10 integer number is:", hex_to_base10(num3))

    elif conversion_type == 4:
        num4 = int(input("What is the hexadecimal number?"), 16)
        print("The binary number is:", hex_to_bin(num4))

    elif conversion_type == 5:
        num5 = int(input("What is the base-10 integer number?"))
        print("The binary number is:", base10_to_bin(num5))

    elif conversion_type == 6:
        num6 = int(input("What is the base-10 integer number?"))
        print("The hexadecimal number is:", base10_10_hex(num6))


def bin_to_hex(num):  # Option 1
    """ This function converts a binary input to a hexadecimal number

       Arguments:
           num (binary): binary number input from start_conversion())

       Returns:
           binary: the now converted hexadecimal number

       Assumptions:
           The user inputs a valid binary value
       """
    num = hex(num)
    return num


def bin_to_base10(num2):  # Option 2
    """ This function converts a binary input to a base-10 integer number

       Arguments:
           num2 (binary): binary number input from start_conversion())

       Returns:
           binary: the now converted base-10 integer number

       Assumptions:
           The user inputs a valid binary value
       """
    num2 = int(num2)
    return num2


def hex_to_base10(num3):  # Option 3
    """ This function converts a hexadecimal input to a base-10 integer number

          Arguments:
              num3 (hex): hexadecimal number input from start_conversion())

          Returns:
              hex: the now converted base-10 integer number

          Assumptions:
              The user inputs a valid hexadecimal value
          """
    num3 = int(num3)
    return num3


def hex_to_bin(num4):  # Option 4
    """ This function converts a hexadecimal input to a binary number

          Arguments:
              num4 (hex): hexadecimal number input from start_conversion())

          Returns:
              hex: the now converted binary number

          Assumptions:
              The user inputs a valid hexadecimal value
          """
    num4 = bin(num4)
    return num4


def base10_to_bin(num5):  # Option 5
    """ This function converts a base-10 integer input to a binary number

          Arguments:
              num5 (dec): base-10 integer number input from start_conversion())

          Returns:
              dec: the now converted binary number

          Assumptions:
              The user inputs a valid base-10 integer value
          """
    num5 = bin(num5)
    return num5


def base10_10_hex(num6):  # Option 6
    """ This function converts a base-10 integer input to a hexadecimal number

             Arguments:
                 num6 (dec): base-10 integer number input from start_conversion())

             Returns:
                 dec: the now converted hexadecimal number

             Assumptions:
                 The user inputs a valid base-10 integer value
             """
    num6 = hex(num6)
    return num6


start_conversion()  # Executes the function
