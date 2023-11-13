var = "Here is some string data with the number two in it."
pswd = "asd213#!sd09"
num = 23423 # Is not a string value so the is methods will not work, as they only work with string
num2 = '23423.468'
space = '     '
#print(len(pswd))
book = "Why I Love To Program With Python"

'''
isupper() and islower()
'''
name = 'ABC'
# print(name.isupper()) # 1  #If all characters are upper case, Python prints True

'''
String methods:
isalpha(): All alpha characters
isalnum(): Combination of alpha and numeric chars.
isdecimal(): Numeric values, not floating point values
isspace(): A space
istitle(): Each word begins with an upper case letter
'''
# print(book.isalpha()) # 2 # cannot manage anything other than letters, including spaces and .
# print(book.istitle())
""" 
print(space.isspace()) # 3
print(str(num).isdecimal()) # 4
print(float(num2)) # 5
print(var.isalnum()) # 6
print(pswd.isalnum()) # 7 # checking pswd 
"""

""" 
# Looking for an alpha character or a space in var variable
count = 0
for i in var:
    if(i.isalpha() == True or i.isspace() == True or i == '.'):
        continue
    else:
        count += 1
        print("Invalid Data")
        break

if(count == 0):
    print("All Data passed validation")
else:
    pass
"""
"""
#startswith() and endswith)
course = 'CSI-160'
if course.startswith('CSI') == True and course.endswith('160') == True:
    print("This is a valid course")
else:
    print("Invalid Course")
"""

"""
Password Validation:
- 8 - 12 Characters
- At least one uppercase letter
- At least one lowercase letter
- At least one special character
- At least one number
"""
def pswd_validator():
    print( "Password Validation")
    print("It must have:")
    print("More than 8 characters")
    print("At least one uppercase letter")
    print("At least one lowercase letter")
    print("At least one special character")
    print("At least one number")
    print("Valid Special Characters: #, !, *, %")
    print("     ")
    chars = ['#', '!', '*', '%']
    upper = False
    lower = False
    num = False
    special = False

    pswd = input("Please input your password: ")
    count = len(pswd)
    if count < 8:
        print("Please be sure to enter more than 8")
        pswd_validator()
    else:
        for j in pswd:
            if j.isupper():
                upper = True # Reassigns the variable a new value
            elif j.islower():
                lower = True
            elif j.isdecimal():
                num = True
            elif j in chars:
                special = True
            else:
                continue
    if upper == True and lower == True and num == True and special == True:
        print("Valid Password")
        exit() # Prevents the execution of code that follows the command
    else:
        print("Process Failed")
        pswd_validator()

pswd_validator()
