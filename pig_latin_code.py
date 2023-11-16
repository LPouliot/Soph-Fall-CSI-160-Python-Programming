# Working with character conversions - words and sentences

"""
ate = ateway is the pig latin translation
frog = rogfay is the pig latin translation
"""

vowels = ['a', 'e', 'i', 'o', 'u']

def choose_process():
    print("Welcome to the Pig Latin Translator")
    print("Enter W for a Word OR S for a Sentence Translation: ")
    choice = input()
    choice.upper()
    if choice == "W":
        chooseWord()
    elif choice == "S":
        chooseSentence()
    else:
        print("Goodbye")
        exit()

choose_process()

def chooseWord():
    print("Please enter your word:")
    text = input()
    if text.isalpha:
        print(convert_word(text))
        choose_process()
    else:
        print("Invalid Input")
        choose_process()

def convert_word(text):
    if text[0].lower() in vowels: # kinda both if-statement and conditionals at the same time
        new_word = text + "way"
    else:
        new_word = text[1:] + text[0].lower() + 'ay'#skip the first letter in the word but grab everything else
                                                    # Force all of the letters to lower
                                                    # and then add ay at the end of the word
    return new_word


def chooseSentence():
    print("Please enter your sentence:")
    sentence = input()
    # Assume the user makes the proper input
    for i in sentence:
        print(sentence)
        choose_process()
    else:
        print("Invalid Input")
        chooseSentence()


def convert_sentence(sentence):
    new_sentence = ""
    length = len(sentence)
    words = sentence.split()  # removing each word and making everything individual
    for word in words:
        new_sentence = new_sentence + convert_word(word) + ""
    new_sentence = new_sentence[0:-1]
    return new_sentence
