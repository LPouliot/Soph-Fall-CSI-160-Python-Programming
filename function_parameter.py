# Working with functions, parameters and placeholders

import math
def start_calc():
    r = int(input("Radius of circle:"))
    return area_of_circle(r) #call this function after the return a function is done, so it does the math and return

def area_of_circle(r1): #to bring the local varible r1 into the function to be used without problems
    p = math.pi
    a = p * math.pow(r1,2)
    return a

print(start_calc()) #after the math is done, it goes back up to the first return



