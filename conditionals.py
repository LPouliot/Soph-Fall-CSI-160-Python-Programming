#working with conditional statements
def ChooseOne():
    x = int(input("Enter an integer value for x:")) #making the input into the interger
    y = 2
    if(x == 0):
        print("The original value of x equals", x)
        x = x + 1
        print("The value of x now equals",x)
    elif(y == 2): # Will only execute if is it wrong, if the statement is true, it will never execute
        print("The Value of 'y' equals",y)
    else:  # For if all else fails, can never tie a condition to an else statement
        print("The conditional failed, y = ",y) # Give information that is informative to the user
#ChooseOne()


def MultiConditions():
    name = input('Enter your name:')
    print("Please enter '1', '2', '3', or '4' to the question below")
    year = input('What year are you in at Champlain College?')
    if(name == "" or year == ""):
        print("please enter your information")
    else:
        print("Welcome")

MultiConditions()



