# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
#difficulty = "1" # sample data, normally the user should choose the difficulty

print("Hello to our Hangman Game!")
print("Please choose a level to start!")

def choosing_level():
    choosing = input("Choose a difficulity (1-3): ")
    while True:
        try:
            choosing_int = int(choosing)
            if choosing_int > 0 and choosing_int < 4:
                return choosing_int
            else:
                choosing = input("Please choose from 1-3: ")
        except ValueError:
            choosing = input("Please choose a number: ")
        
choosing_int = choosing_level()

print(f"You choosed the difficulity {choosing_int}.")

def lives(choosing_int):
    lives = 0
    if choosing_int == 1:
        lives = 15
            #import smaller word
    elif choosing_int == 2:
        lives = 13
            #import longer word
    else:
        lives = 11
            #import longest word
    return lives

lives = lives(choosing_int)
print(f"You have {lives} lives.")



def country_or_capital():
    country_or_capital = input("Choose from countries or capitals with 'CNT' or 'CPT': ")
    while True:
        if country_or_capital == 'CNT':
            return 0
        elif country_or_capital == 'CPT':
            return 1
        else:
            print("Choose from 'CNT' or 'CPT'")

CNT_or_CPT = country_or_capital()

import random

def random_line():
    f = open("countries-and-capitals.txt", "r")
    file_content = f.read()
    word_list = file_content.split('\n')
    word_line = random.choice(word_list)
    return word_line.upper()

word_line = random_line()
print(word_line)

def choosen_word (CNT_or_CPT, word_line):
    word_line_split = word_line.split('|')
    if CNT_or_CPT == 0:
        return word_line_split[0]
    else:
        return word_line_split[1]

word = choosen_word(CNT_or_CPT,word_line)
print(f"The choosen word is {word}") 


# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txt
lives = 5 # sample data, normally the lives should be chosen based on the difficulty




# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"

def play(word_to_guess):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = lives


# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions

def guess(letter):
    input("Please guess a letter or word: ").upper()

# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
already_tried_letters = [] # this list will contain all the tried letters


# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".


# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.



# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4
