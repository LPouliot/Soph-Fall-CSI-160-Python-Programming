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

