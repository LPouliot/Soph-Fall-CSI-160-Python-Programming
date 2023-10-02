# Working with Loops

mixedList = ["john","sally","sam","Larry","Mary", 1, 2, 6, 7, 9, 0, 2, 4, 5]
title = "Python Programming"

for i in mixedList:
    print("The item in the next list is:",i)

spam = 0
if spam < 5:
    print("Hello World")
    spam = spam + 1
else:
    print("You fail if you forget the Else Statement!")


# The 'while' loop
x = 0
while x < 5:
    print(x)
    x = x + 1


for j in range(5): # The 5 indicates to loop from zero and up to but not include the value in the function
    print(j) # j is a placeholder

for k in range(-5,5): # The loop starts at -5 and goes up to but include 5
    print(k)

for l in range(10,-20,-2): # The first value is the starting point, the second value is the "up to but not include" value
                        # the third value is the incrementor (for this example, we are counting by 2's)
    print(l)


