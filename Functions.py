# Working with Functions
"""
Naming as the same as variables
must start with the key word "def" and must always be lowercase
def test_function():
TestFunction():
Follow the name instructions, so it is properly named

Once pressing enter, the curser is indented

pass --> putting in a placeholder, not ready to enter code, just to avoid kickbacks
Keep interpreter from recognizing an error
"""


def test_function():
    pass


"""
If you were still in the function, when you hit enter after pass, it would still be indented and not in the margin 
"""


"""
def PrintText():
    print('Here is some string')
    x = 1
    print('The value of x equals', x)
    y = 3
    z = x + y
    print(z)
    
PrintText()  # This is a function call
"""
# To get out of the function, hit backspace

z = ""
x = 1
y = 0
def var_mgt(): # Keep the name descriptive but simple
    global x
    x = x + 1
    print('The value of x equals', x)
    yy = 3
    zz = x + yy
    print('The value of all the numbers equals:',zz)

var_mgt()

def x_vale():
    global x # needs to be declared before anything else is done in the function
    x = x + 1
    print('Changing the number once again')
    print(x)  # The values of the global variable x was overriden by the global x commands in the var_mgt function

x_vale()







