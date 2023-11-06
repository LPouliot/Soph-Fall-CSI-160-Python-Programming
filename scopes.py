# Understanding variable scope
import math
import my_modules

y = 0 # Global variable, available to all functions. Problems are encountered when the global
      # Variable is used in a function and its value is changed

def my_function():
    global y #allows y into the function
    y = y + 2 # Not allowed due to the fact that code is changing the value of a global variable
    x = 1 # local variable, only accessible to this function

#An example of encapsulating scope
def outside_function():
    x2 = 2 # Every Variable MUST BE DIFFERENT, no duplicates!
    print("This is the outside_function()", x2)


    def inner_function():
        x2 =10
        print("This is the inner_function()", x2)
    inner_function()

# outside_function()

def use_math():
    r = int(input("Radius: "))
    area = r**2*my_modules.p # The variable 'p' sits in the my_modules file.
                             # Prefix the calling of this variable by its module location
    print("The area of a square equals:", area)

use_math()

for i in my_modules.x:
    print(i)



