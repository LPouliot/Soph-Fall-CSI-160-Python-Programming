# This is a comment, the interpreter will not process it as code.
# To create a block comment, use quote marks


"""
Here is a block comment
it takes up two lines
"""

'''
Here is another block comment
using a series of single quotes
Do "" or '' twice and then press enter
'''


'''
A varible
num1 = 2
num2 = "8"

result = num1 * num2
result = num2/num1 #Varible reassignment
result2 = num1 / num2 #dividing

print(result)
print(result2)
'''


'''
name = "John Doe"
# It has to be in quotes because it's a string. Text cannot be a float/interger/boolean
address = '1 Main Street'
# nesting quote marks --> quotes within quotes that are printed with the string
title = "Book = 'Python Programming'"
age = 22 # interger data type

print(name + "is" + str(age) + "years old.") #mixing string with variable output
# concatination, when you pull together your string and varible information. Plus ( + )is a concatnator
print(name, "is",age,"years old.")
# Instead of using +, using commas make it a lot better and spaces things out better
'''


"""
first_name = input("Enter your name:")
n1 = int(input("Enter your first number:"))
n2 = int(input('Enter your second number:'))
# O r,  n2 =int(n2)   n1 = int(n1)
# That is another option in order to turn the string into an interger
n3 = n1 + n2
print("Hi",first_name,"The addition of these numbers equals",n3)

length = len(title)
print("The number of characters in the variable 'title' equals:",length)
# The single quote marks are counted as string
"""

courses = 5
grade1 = 3.75
grade2 = 3.25
grade3 = 3.01
grade4 = 3.00
statement = "Hello, your GPA average this year is"

grade5 = float(input("Enter your 5th class GPA:"))
sum = (grade1 + grade2 + grade3 + grade4 + grade5)
avg = sum / courses
avg1 = sum // courses
print(statement,avg)
print(statement,"And rounded is",avg1)



