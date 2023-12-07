"""
Author: Lily
Class: CSI-160-01
Assignment: Final Project
Due Date: 12/6/23

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

"""
To get everything started and can cycle back here when the game is over
"""
def the_welcome():
    print("Welcome to The Manor Game!")
    ready = input("Ready to play the game? (y/n): ")
    if(ready == 'y'):
        the_plot()
    else:
        print("Okay Goodbye")

"""
To address the plot and makes sure the user is ready to play
"""
def the_plot():
    print("You are a detective who works for a small town.\n"
    "The department sends you out to a manor living on the outskirts of town to solve a case.\n"
    "You are tasked to find the person who killed the owner of the mansion.\n"
    "When ready, you can exit the house and enter your guess of who the killer was.")
    start = input("Type start when you are ready: ")
    if(start == 'start'):
        the_beginning()
    else:
        print("Please try again")
        the_plot()

"""
Gives the user the options on where to go
"""
def the_beginning():
    print(" - - - - ")
    print("You find yourself in the hallway, you can:")
    print("1 - Exit the House\n"
          "2 - Enter the Living Room\n"
          "3 - Enter the Kitchen\n"
          "4 - Enter the Bedroom\n"
          "5 - Enter the Garden\n"
          "6 - Open your bag")
    num = input("Enter your number here: ")
    if(num == '1'):
        exit_house()
    elif(num == '2'):
        living_room(itemsInBag)
    elif(num == '3'):
        the_kitchen(itemsInBag)
    elif(num == '4'):
        the_bedroom()
    elif(num == '5'):
        the_garden(itemsInBag)
    elif(num == '6'):
        open_bag(itemsInBag)
"""
This is at the end of the game where the user guesses who is the murderer
If they choose correctly then the game is over
If not, then they have to restart the game
"""
def exit_house():
    print("You have now exited the house and may know who the murderer is.")
    print("Who did it?")
    print("1 - The Gardener \n"
          "2 - The Cook \n"
          "3 - The Wife \n"
          "4 - The Butler ")
    guess = input("Please enter a number: ")
    while True:
        if(guess == '1'):
            print("Congrats! You have found the Murderer!")
            print("You make a great detective")
            print("GAME OVER")
            end = input("Type OK to end the game: ")
            if(end == "OK"):
                exit()
            else:
                continue
        else:
            print("They were not the murderer")
            again = input("Type again to try once more: ")
            if(again == "again"):
                print(" - - - - ")
                the_welcome()
            else:
                print("Still trying again")
                print(" - - - - ")
                the_welcome()

"""
Lets user enter a 'room' to explore and search for clues. There is a while loop embedded
the loop is to make sure the user is ready to move on 
"""
def living_room(itemsInBag):
    print("You find yourself in a lavish living room with dramatic mirrors, paintings, and a crystal chandelier.\n"
          "The Butler, sporting an expensive suit, was busy dusting one of the counters.\n"
          "He muttered something under his breath while focusing on his work.\n"
          "His attention eventually shifted as you entered the room.")
    print(" - - - - ")
    print("You could look at the options below or exit the room.")
    print("1 - The Bookshelves\n"
          "2 - The Furniture\n"
          "3 - The Butler\n"
          "4 - The Ottoman\n"
          "5 - Exit Room")
    num1 = input("Please enter a number: ")
    while True:
        if (num1 == '1'):
            print("There are plenty of old books, all ranging from modern to old classics.\n"
                  "However, a book is missing from the shelf, as there is space at the top-left corner.")
            ready = input("Please type ready when you are ready to move on: ")
            if(ready == "ready"):
                print(" - - - - ")
                living_room(itemsInBag)
            else:
                continue

        if (num1 == '2'):
            print("There wasn't anything useful near the furniture.\n"
                  "but it provided a comfortable place to sit down and think for a few minutes.")
            when = input("Please type ready when you are ready to move on: ")
            if (when == "ready"):
                print(" - - - - ")
                living_room(itemsInBag)
            else:
                continue

        if (num1 == '3'):
            print("The Butler seemed busy watering the plants near the windowsill before focusing on you.")
            print("``Greetings detective. I do hope you will find this killer.``\n"
                  "``If this is any help, the ottoman has a locked box.``\n"
                  "``I cannot seem to get into it``")
            whene = input("Please type ready when you are ready to move on: ")
            if (whene == "ready"):
                print(" - - - - ")
                living_room(itemsInBag)
            else:
                continue

        if (num1 == '4'):
            print("A beautiful mahogany ottoman sits on the wall beside the main entrance.\n"
                  "There appears to be a wooden box sitting on the ottoman with a code keeping it locked.")
            locked = input("Do you have an ottoman code in your bag? (y/n)")
            if (locked == "y"):
                key = input("Enter the code here: ")
                if (key == "736"):
                    print("The box clicked open, revealing the missing book from the shelf.\n"
                          "It was about exotic and common plants found around the town.")
                    bag = input("Do you want to put it in your bag? (y/n): ")
                    if (bag == "y"):
                        itemsInBag.append("Exotic Plant Book")
                        print("You now have", itemsInBag)
                        whener = input("Please type ready when you are ready to move on: ")
                        if (whener == "ready"):
                            print(" - - - - ")
                            living_room(itemsInBag)
                        else:
                            continue
                else:
                    print("That is the wrong code")
                    living_room(itemsInBag)
            else:
                print("You should probably find that code")
                print(" - - - - ")
                living_room(itemsInBag)

        if (num1 == '5'):
            print("You exit the room")
            the_beginning()
        else:
            print("Try again")
            living_room(itemsInBag)

"""
Lets user enter a 'room' to explore and search for clues. There is a while loop embedded
the loop is to make sure the user is ready to move on 
"""
def the_kitchen(itemsInBag):
    print("You find yourself in a large kitchen coated in the smell of roasted duck simmering in the oven.\n"
          "Beside the counter is a busy chef chopping vegetables on a flat wooden board.\n"
          "Her skills with the knife catch your attention.\n"
          "She aggressively but efficiently slices a couple of veggies in a matter of seconds.")
    print(" - - - - ")
    print("You could look at the options below or exit the room.")
    print("1 - The Fridge\n"
          "2 - The Cook\n"
          "3 - The Cabinets \n"
          "4 - Exit Room ")
    num2 = input("Please enter a number: ")
    while True:
        if (num2 == '1'):
            print("You couldn’t find much in the fridge, but a bunch of expensive produce was found inside.\n"
            "``HEY out of the fridge! You’re going to warm everything up!``\n"
            "You swiftly closed the fridge after the cook yelled at you")
            whee = input("Please type ready when you are ready to move on: ")
            if (whee == "ready"):
                print(" - - - - ")
                the_kitchen(itemsInBag)
            else:
                continue

        if (num2 == '2'):
            print("The chef lowered the knife before turning her attention to you.\n"
                  "``Here to investigate the murder? Feel free to look around.``\n"
                  "``Just- not the fridge since I got some important stuff in there``")
            whe = input("Please type ready when you are ready to move on: ")
            if (whe == "ready"):
                print(" - - - - ")
                the_kitchen(itemsInBag)
            else:
                continue

        if (num2 == '3'):
            print("The Cabinets on the far end of the kitchen held a few bottles that were labeled,\n"
                  " “Keep out, G’s items” \n"
                  "You cannot see what is inside of the bottles due to the foggy glass")
            put = input("Do you want to put it in your bag? (y/n): ")
            if (put == "y"):
                itemsInBag.append("Unlabeled Bottles")
                print("You now have", itemsInBag)
                whener = input("Please type ready when you are ready to move on: ")
                if (whener == "ready"):
                    print(" - - - - ")
                    the_kitchen(itemsInBag)
                else:
                    continue

        if (num2 == '4'):
            print("You exit the room")
            the_beginning()
        else:
            print("Try again")
            the_kitchen(itemsInBag)

"""
The user has to use the code in order to enter the actual bedroom
"""
def the_bedroom():
    print("The door to the bedroom is locked.\n"
          "Despite your attempts to open it, you realize you need a code.")
    codee = input("Do you have a bedroom code in your bag? (y/n)")
    if (codee == "y"):
        keyy = input("Enter the code here: ")
        if (keyy == "901"):
            print("After trying out the code, you can hear the door click and swing open.")
            print(" - - - - ")
            real_bedroom(itemsInBag)
        else:
            print("That is the wrong code")
            print(" - - - - ")
            the_bedroom()
    else:
        print("You should probably find that code")
        print(" - - - - ")
        the_beginning()

"""
Lets user enter a 'room' to explore and search for clues. There is a while loop embedded
the loop is to make sure the user is ready to move on 
"""
def real_bedroom(itemsInBag):
    print("You are now in a large dusty room, clouded by the heavy drapes that block most of the light.\n"
          "The well-kept space with pristine decor and furniture couldn’t compare to the heavy mourning feeling.\n"
          "Sitting at one of the plush chairs held a sickly lady, the wife of the victim.\n"
          "She watched you enter the room with a lifeless stare.")
    print("You could look at the options below or exit the room.")
    print("1 - The Closet\n"
          "2 - The Wife\n"
          "3 - The Desk\n"
          "4 - Exit Room ")
    num3 = input("Please enter a number: ")
    while True:
        if (num3 == '1'):
            print("Inside the wooden closet are neatly hung coats and shirts worn by the previous owner.\n"
                  "After a thorough examination, you were not able to find any clues.\n"
                  "However, you did find a very nice hat.")
            why = input("Should you take the hat? (y/n): ")
            if (why == "y"):
                itemsInBag.append("Very Nice Hat")
                print("You now have", itemsInBag)
                wh58e = input("Please type ready when you are ready to move on: ")
                if (wh58e == "ready"):
                    print(" - - - - ")
                    real_bedroom(itemsInBag)
                else:
                    continue
            else:
                print("You left the very nice hat alone")
                print(" - - - - ")
                real_bedroom(itemsInBag)

        if (num3 == '2'):
            print("The widow silently sat in the felted armchair, her face wrinkled from age and sorrow.\n"
                  "Eventually, a crackling voice emitted from her,\n"
                  "``The desk. It holds a clue..``\n"
                  "She didn’t provide any context after that, returning to her lifeless stare.")
            wh5e = input("Please type ready when you are ready to move on: ")
            if (wh5e == "ready"):
                print(" - - - - ")
                real_bedroom(itemsInBag)
            else:
                continue

        if (num3 == '3'):
            print("You made your way over to the wooden desk with a thin polished stone plate as decoration.\n"
                  "There is a locked compartment beneath the desk that requires a code.\n"
                  "However, a paper rests on the top of the desk.\n"
                  "It may have what you need.")
            read = input("Read the paper? (y/n): ")
            if(read == 'y'):
                print("You find yourself reading a math equation. \n" ""
                      "Perhaps using the answer as the code will get what you need.\n"
                      "The math equation is: 9 × 8 + 4 − 2 ÷ (4 − 2)")
                ans = input("Enter your answer here: ")
                if(ans == '75'):
                    print("The compartment clicked open, revealing a folded paper with another code on it.")
                    take = input("Take the new code? (y/n): ")
                    if(take == 'y'):
                        itemsInBag.append("Ottoman Code (736)")
                        print("You now have", itemsInBag)
                        wh55e = input("Please type ready when you are ready to move on: ")
                        if (wh55e == "ready"):
                            print(" - - - - ")
                            real_bedroom(itemsInBag)
                        else:
                            continue

                    else:
                        print("You left the code alone")
                        print(" - - - - ")
                        real_bedroom(itemsInBag)

                else:
                    print("Wrong answer")
                    continue

            else:
                print("You left the paper alone")
                print(" - - - - ")
                real_bedroom(itemsInBag)


        if (num3 == '4'):
            print("You exit the room")
            the_beginning()
        else:
            print("Try again")
            real_bedroom(itemsInBag)

"""
Lets user enter a 'room' to explore and search for clues. There is a while loop embedded
the loop is to make sure the user is ready to move on 
"""
def the_garden(itemsInBag):
    print("You are now in a rather small space covered by large window panes that allow light to flood through.\n"
          "The area smells like the jungle due to the humid air and mass amount of plants.\n"
          "Despite being a cramped space,\n"
          "you find a gardener easily weaving through the large pots and watering the plants.\n"
          "He notices you walk in and gives a welcoming greeting.")
    print("You could look at the options below or exit the room.")
    print("1 - The Gardener\n"
          "2 - The Large Plants\n"
          "3 - The Shelving Units\n"
          "4 - Exit Room ")
    num4 = input("Please enter a number: ")
    while True:
        if(num4 == '1'):
            print("You make your way to the gardener\n"
                "``Welcome to the manor. I hope you are finding plenty of clues and enjoying your stay.``\n"
                "``Would you like some tea?``")
            tea = input("Do you take the tea?(y/n): ")
            if(tea == "y"):
                print("You took the steamy cup of tea from the gardener's hand.\n"
                      "The taste of the tea is something you do not recognize.")
                wh556e = input("Please type ready when you are ready to move on: ")
                if (wh556e == "ready"):
                    print(" - - - - ")
                    the_garden(itemsInBag)
                else:
                    continue

            else:
                print("You decline the offer and get back to work")
                wh599e = input("Please type ready when you are ready to move on: ")
                if (wh599e == "ready"):
                    print(" - - - - ")
                    the_garden(itemsInBag)
                else:
                    continue

        if(num4 == '2'):
            print("After a bit of searching through all of the large plants, you were not able to find anything. \n"
                "You did enjoy looking at all of the colorful fruits and vegetables that were being grown.")
            wh59e = input("Please type ready when you are ready to move on: ")
            if (wh59e == "ready"):
                print(" - - - - ")
                the_garden(itemsInBag)
            else:
                continue

        if(num4 == '3'):
            print("Through some extensive searching, you discovered a little space behind a few potted succulents.\n"
                  "After moving the pots away, you find a hidden compartment.\n"
                  "Inside was a folded piece of paper with a written code.")
            takes = input("Do you take the code? (y/n): ")
            if (takes == 'y'):
                itemsInBag.append("Bedroom Code (901)")
                print("You now have", itemsInBag)
                wh55e = input("Please type ready when you are ready to move on: ")
                if (wh55e == "ready"):
                    print(" - - - - ")
                    the_garden(itemsInBag)
                else:
                    continue

            else:
                print("You left the code alone")
                print(" - - - - ")
                the_garden(itemsInBag)


        if (num4 == '4'):
            print("You exit the room")
            the_beginning()
        else:
            print("Try again")
            the_garden(itemsInBag)


"""
Used and modified the backpack lab from week 6.
Shows items from the bag, allows user to check if items are in the bag,
allows items to be added, exits back to  the_beginning function
"""
itemsInBag = ["book", "magnifying glass", "keys", "notebook", "pen"]
def open_bag(itemsInBag):
    while True:
        print("Would you like to:")
        print("1 - See what's in your bag?")
        print("2 - Add an item to the bag?")
        print("3 - Check if an item is in the bag?")
        print("4 - Quit")
        userChoice = input()
        if userChoice == '1':
            print(itemsInBag)
        elif userChoice == "2":
            print("What item do you want to add to the bag?")
            itemToAdd = input()
            itemsInBag.append(itemToAdd)
            print("You now have", itemsInBag)
        elif userChoice == "3":
            print("What item do you want to check to see if it is in the bag?")
            itemToCheck = input()
            if itemToCheck in itemsInBag:
                print("Yup! It's all packed and ready to go")
            else:
                print("Nope- It's not in there")
        elif userChoice == "4":
            the_beginning()

the_welcome()
