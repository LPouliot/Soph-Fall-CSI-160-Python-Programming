# Working with try...except

def calc_reciprocal():
    x = int(input('Enter a number: '))
    try:
        z = 1/x
        print(z)
        again = input("Do you want to try again? (y/n): ")
    except Exception as e:# Must be capitalized
        print('There was an error detected:', e)
        calc_reciprocal()

calc_reciprocal()



