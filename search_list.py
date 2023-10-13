# Develop code that will allow a user to input a letter. Search for the letter. Return its index position
# and how many times it was found in the list. if it is not in the list, let the user know it was not
# found in the list. Ask if the user would like to add it to the list. If yes, add it. If no, end.
letters = ['a', 'w', 'q', 'a', 's', 'd', 'c', 'z', 's']

guess = (input("Guess a letter in our list: "))
def searchlist(guess):
    count = 0
    for i in letters:
        if(i == guess):
            count = count + 1
        else:
            continue
    if(count > 0):
        print("The letter", guess, "was found", count,"times")
        print("The index position(s) of the letter are located at:")
        for idx, i in enumerate(letters): #We went over it in the meeting, where this finds the index(s) easily 
            if i == guess:
                print(idx)
    elif(count == 0):
        print("This letter was not found in our list")
    else:
        print("The letter was not found")
searchlist(guess)
