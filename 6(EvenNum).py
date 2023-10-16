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
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def print_even(numbers):
    """Prints the even numbers in a list, one per line

    :param numbers: (list) list of integers
    :return: None
    """
    for i in numbers:
        if (i % 2) == 0: # Since evens have a remainder of 0 when divided by two, it will append to the list
            print(i)
        else:
            continue

print_even(numbers)
