"""
Author: Lily
Class: CSI-160-01
Assignment: Week 10/11 Lab
Due Date: 11/10/23

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
Password complexity check
- Input from user for their password
- Checks to see if it has the required parameters 
- Once it has all of the requirements, returns the password 
- Returns the checked password 
"""
def pass_validator():
    print("Password Validation")
    chars = ['#', '!', '*', '%', '^', '@', '.', ',', '?', '/', '|', ':', ';', '~', '`']
    upperL = False
    lowerL = False
    num = False
    special = False

    while True:
        print("Hello, You need to make a password for us to encrypt")
        print("It needs to have...")
        print("At least one uppercase letter")
        print("At least one lowercase letter")
        print("At least one special character")
        print("At least one number")
        print("Not all Special Characters Will Work")
        print("       ")
        password = input("Please input your password: ")

        if len(password) >= 8:
            for j in password:
                if j.isupper():
                    upperL = True
                elif j.islower():
                    lowerL = True
                elif j.isdecimal():
                    num = True
                elif j in chars:
                    special = True
                else:
                    continue

            if upperL and lowerL and num and special:
                print("Valid Password")
                return password
            else:
                print("Invalid Password. Please try again.")
                upperL = lowerL = num = special = False
        else:
            print("Please be sure to enter a password with more than 8 characters")

validated_password = pass_validator() # Had to make the return of the function into a variable in order to use it

print("          ")
print("Password Used:", validated_password)
print("          ")

"""
Ability to edit an entry
- Check to see if this is the password they want to use
- Ask if they want to change the password 
- Lets them change the password and ask if they are happy with it
- Checks to make sure it fits with the standards 
"""
def edit_entry():
    while True:
        try:
            question = input("Are you happy with your new password? (y/n): ")
            if question == "y":
                print ("Perfect, we will continue then")
                break
            elif question == "n":
                print("Okay you can add a new password")
                pass_validator()
            else:
                print("Please try again")
        except ValueError as e:
            print(e)

edit_entry()

"""
Add Entry
- The ability to add new entries to the password manager.
- Needs to encrypt the password. 
- (A friend from UVM who is also taking python helped me create a script to encrypt the password) 
- returns the cipherText that was created in the function 
- I tried to make it so it also adds numbers and special characters but I was not able to figure it out
"""

shift = int(input("How far would you like to shift the cypher: "))
def encrypt_Pass(validated_password,shift):
    try:
        cipherText = ""
        for ch in validated_password:
            if ch.isalpha():
                stayInAlphabet = ord(ch) + shift # "shift" is how far I want it to shift by (The key)
                if stayInAlphabet > ord('z'): # Ord turns normal characters in ASCII
                    stayInAlphabet -= 26
                finalLetter = chr(stayInAlphabet) # Chr turns the ASCII into normal characters
                cipherText += finalLetter
        print ("Your ciphertext is: ", cipherText)
        return cipherText
    except ValueError as p:
        print("An error occurred:", p)
        return None  # to handle error without returning the encrypted Text

new_password = encrypt_Pass(validated_password,shift) # Had to make the return of the function into a variable in order to use it

"""
Lookup Entry
- Needs to decrypt the password.
- Added a function called asking_question to see if the user wanted to decrypt the password 
- Used the name encrypting script above but changed it to decrypt instead 
- returns the decryptText that was created in the function 
- I tried to make it so it also adds numbers and special characters but I was not able to figure it out
"""
def asking_question():
    while True:
        try:
            question = input("Would you like to decrypt the password? (y/n): ")
            if question == "y":
                question_shift = int(input("How far would you like to shift the cypher: "))
                return question_shift
            elif question == "n":
                print("Okay Bye!")
                break # To exit the loop if the user wants to end
            else:
                print("Please try again")
        except ValueError as i:
            print(i)

shift2 = asking_question() # Had to make the return of the function into a variable in order to use it

def decrypt_Pass(new_password, shift2):
    try:
        decryptedText = ""
        for ch in new_password:
            if ch.isalpha():
                stayInAlphabet = ord(ch) - shift2  # "shift2" is how far you want to shift by (The key)
                if stayInAlphabet < ord('a'):  # Ord turns normal characters in ASCII
                    stayInAlphabet += 26
                finalLetter = chr(stayInAlphabet)  # Chr turns the ASCII into normal characters
                decryptedText += finalLetter
        print("Your decrypted text is:", decryptedText)
        return decryptedText
    except Exception as y:
        print("An error occurred:", y)
        return None # to handle error without returning the decrypted Text

decrypt_Pass(new_password,shift2)
