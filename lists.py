#working with lists

x = [] #empty list

x = ['a', 'b', 3, True, 9.89]
print(x)

#How to get only one of the indexes, for example, b
print(x[1])


# Working with the 'for' loop
for i in x: #The 'i' is a varible. The loop will pass a value from the list 'x' to 'i'
    print(i) #Prints  the current value of 'i'
# Will only loop for as many items in the list until the list runs out, from first to last


length = len(x) #The len fuinction here is counting the number of items in the list
print(length)

mylist = [1, 2, 6, 7, 9, 0, 2, 4, 5]
new_list = x + mylist  #list concatenation
print(new_list)

y = new_list[4:5] #asks for a range of output. The output starts with the vaule in the second index position
                  # It includes all values up to BUT DOES NOT INCLUDE the value of the last index position
                  # This is called a 'slice'.
print("The contents of the new_list are:",new_list)
print(y)

#Pulling items from a list based on negative index value
print(mylist[-2]) #if negative index value is used, it will pull from the end of the list.
                  # This pulls out the second item of the list

print(mylist[-2:1]) #Starting a slice with a negative value ends up returning an empty list

names = ["John", "Sally", "Sam"]
names[2] = "Chris" #The value of "Sam" was replaced by "Chris"
print(names)

names.remove("Chris") #The Remove() will remove an item named in the function
                    # of "Chris" is gone. You cannot pass the value you remove to a variable
                    # Pass the value to a variable before it is removed
print(names)

names.append("Sam") #adds the value in the () to the end of the list
print(names)

names.insert(10,"Keith") # This inserts a value at the specific index position in the list
                        # The 1st Value must be in the index position and the 2nd is the item
print(names)
pos1 = names.index("Keith") #  index that acceeds the list, it will assign it to the end (for this it's the 3rd)
print(pos1)

print(names)
names.sort() # Capitalized words come first in the sort (but I already made mine all caps, so they are alphabetized
print(names)
names.sort(reverse = True) # Preforms a reverse sort
print(names)

names.sort(key = str.lower) # Sorts by strict alphabetic rules
print(names)

# mylist = [1, 2, 6, 7, 9, 0, 2, 4, 5]

del mylist[4] #Deletes the item according to the index position noted
print(mylist)

print(mylist) #This shows the items are they are in the list
mylist.sort()
print(mylist) #This shows the sorted list

mixedList = ["john","sally","sam","Larry","Mary","1","2"]
mixedList.sort() # String numbers get sorted first, followed by capitalized names
                    # followed by lower case names
print(mixedList)
