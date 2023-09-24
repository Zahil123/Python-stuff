import random
from dict import words
import string

def get_valword(words):

    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def construct():

    print("\t\tWELCOME TO HANGMAN")
    word = get_valword(words)   #Gets a valid word
    word_letters = set(word)    #Stores the individual letters in the word
    alphabet = set(string.ascii_uppercase)  #Stores letters A-Z
    used_letters = set()    #Stores the letters the user has entered

    lives = 6

    while len(word_letters)>0 and lives>0:

        #Letters used printed
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("Letters used: ", ' '.join(used_letters))
        print("Lives left: ", lives)

        #What the current word is (W _ R D )
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list)) 

        user_letter = input("Guess a letter: ").upper()     #Taking user input

        if(user_letter in alphabet - used_letters):
            used_letters.add(user_letter)
            if(user_letter in word_letters):
                word_letters.remove(user_letter)

            else:
                lives = lives-1
                print("Letter is not in word")

        elif(user_letter in used_letters):
            print("Letter has already been used")

        else:
            print("Invalid character. Please try again")
        print("\n")
    
    if lives == 0:
        print("Game over!\nThe word is ",word)
    else:
        print("You won!\nThe word is ",word)
    print("\n")

construct()