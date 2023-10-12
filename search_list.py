# Searching for certain indexes in a list

letters = ['a', 'w', 'q', 'a', 's', 'd', 'c', 'z', 's']
# Develop coe that will allow a user to input a letter. Search for the letter. Return its index position
# and how many times it was found in the list. if it is not in the list, let the user know it was not
# found in the list. Ask if the user would like to add it to the list. If yes, add it. If no, end.

guess = (input("Guess a letter in our list:" ))
# guess = 'a'
def searchlist():
    count = 0
    for i in letters:
        if(i == guess):
            count = count + 1
        else:
            continue
    print(count)
    if(count > 0):
        print("The letter", guess, "was found", count,"times")
    elif(count == 0):
        print("The letter was not found")
    else:
        print("This letter was not found in our list")

searchlist()
