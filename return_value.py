#Using 'return' in a function
def calc1():
    x = 1
    y = 2
    z = 3
    print("This is from the calc1 function:",z)

def calc2():
    x = 5
    y = 2
    z = x * y
    return z #The result of the operation is held in memory. The function call results
                # In the ANSWER becoming avaible for use

calc1()
print(calc2()*5)

