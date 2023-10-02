# Working with conditionals and loops

mixedList = ["john","sally","sam","Larry","Mary", 1, 2, 6, 7, 9, 0, 2, 4, 5]
title = "Python Programming"

# Searching for an item in a list
def searchList():
    count = 0
    for i in mixedList:
        if(i == "sam"):
            count = count + 1
            item = i
        else:
            continue
    if(count == 0):
        print("The item was not found")
    elif(count > 0):
        print("The item", item,"was found. It was found", count,"times")
    else:
        print("Process failed, please try again")

searchList()

"""
Data Validation:
isdigit() -> determines if a string value is an integer or not an integer 
isalpha() -> determines if a string value is composed of all alpha (letters) characters
"""
def sortList():
    strings = []
    numbers = []
    strings = mixedList[0:5]
    numbers = mixedList[5:]
    print(strings)
    print(numbers)
sortList()



