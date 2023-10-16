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
listToPrint = []
while True:
    newWord = input("Enter a word to add to the list (press return to stop adding words): ")
    if newWord == "":
        break
    else:
        listToPrint.append(newWord)
print(listToPrint)

def adding_and(list):
    string = '' # Temporary storage for string, trying to add it to an empty list will not work
    for i in list:
        string = string + str(i) # Using the string converter function to append old items into new storage
        if list.index(i) == (len(list)-2): # I had help with this from a friend back in my hometown
                                           # -2 makes it go to the second to last number and index helps find the place
                                           # in the list while the len function counts the number of spots in the list
            string = string + ', and ' # If the item is the second to last, it will add and
        elif list.index(i) == (len(list)-1): # -1 gets the end of the list and the len function helps
            continue
        else:
            string = string + ', ' # In any other situation, append the coma
    return string

print(adding_and(listToPrint)) # calling the function. I also had help with this since the function calling was not working




