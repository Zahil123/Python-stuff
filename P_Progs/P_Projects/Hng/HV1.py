import random
from dict import words
import string

l=h=lives=0
i=1

def get_valword(words,l,h):


    while i<len(words):
        word = random.choice(words)
        length = len(word)
        if (length>=l) and (length<=h):
            w = set(word)
            if '-' in w or ' ' not in w:
                return word.upper()

        else:
            continue

    '''for i in range (len(words)):             Searches for a word linearly
        word = words[i]
        length = len(word)                      Will choose the same word each time for each setting
        if (length>=l) and (length<=h):
            w = set(word)
            if '-' in w or ' ' not in w:
                return word.upper()'''
    
def construct():

    print("\t\tWELCOME TO HANGMAN")

    ch = input("\n\nChoose difficulty(E/M/H): ")

    if ch == 'e' or ch == 'E':
        lives = 15
        l = 2
        h = 4
    
    elif ch == 'm' or ch == 'M':
        lives = 10
        l = 5
        h = 7
    else:
        lives = 5
        l = 8
        h = 10

    word = get_valword(words,l,h)   #Gets a valid word
    #print(word)
    word_letters = set(word)    #Stores the individual letters in the word
    alphabet = set(string.ascii_uppercase)  #Stores letters A-Z
    used_letters = set()    #Stores the letters the user has entered

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