
def choosing_level():
    choosing = input(f"{bcolors.WARNING}Choose a difficulity (1-3): ")
    while True:
        try:
            choosing_int = int(choosing)
            if choosing_int > 0 and choosing_int < 4:
                return choosing_int
            else:
                choosing = input("Please choose from 1-3: ")
        except ValueError:
            choosing = input("Please choose a number: ")


def lives_value(choosing_int):
    lives = 0
    if choosing_int == 1:
        lives = 9
    elif choosing_int == 2:
        lives = 8
    else:
        lives = 7
    return lives


def country_or_capital():
    country_or_capital = input(f"{bcolors.WARNING}Choose from countries or capitals with 'CNT' or 'CPT': ").upper()
    while True:
        if country_or_capital == 'CNT':
            return 0
        elif country_or_capital == 'CPT':
            return 1
        else:
            country_or_capital = input("Choose from 'CNT' or 'CPT'").upper()

import random

def random_line():
    f = open("countries-and-capitals.txt", "r")
    file_content = f.read()
    word_list = file_content.split('\n')
    word_line = random.choice(word_list)
    f.close()
    return word_line

def choosen_word (CNT_or_CPT, word_line):
    word_line_split = word_line.split(' | ')
    if CNT_or_CPT == 0:
        return word_line_split[0]
    else:
        return word_line_split[1]

def display(word_to_guess):
    secret_word = []
    for i in word_to_guess:
        if i == " ":
            secret_word.append(" ")
        else:
            secret_word.append("_")
    return secret_word

def validate(already_tried_letters):
        guess_letter = input(f"{bcolors.WARNING}Please guess a letter or word: ").upper()
        while True:
            if guess_letter in already_tried_letters:
                print("You already guessed this letter!")
                guess_letter = input("Try an other one: ").upper()
            else:
                already_tried_letters.append(guess_letter)
                return guess_letter

def present(guess, word_to_guess, secret_word:list, lives):
    f = open("ascii_art.py", "r")
    file_content = f.read()
    pictures = file_content.split(",")
    new_secret_word = []
    if guess in word_to_guess.upper():
        print(f"{bcolors.FAIL}Lives: {lives}")
        for i in range(len(word_to_guess)):
            if word_to_guess[i].upper() == guess:
                new_secret_word.append(word_to_guess[i])
            else:
                new_secret_word.append(secret_word[i])
        secret_word = new_secret_word
        return secret_word, lives
    else:
        lives -= 1
        print(f"{bcolors.FAIL}Lives ", lives)
        print(pictures[8 - lives])
    f.close()
    return secret_word, lives

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    print("\n" * 5)
    print(f"{bcolors.OKGREEN}""Hello to our Hangman Game!")
    print(f"{bcolors.HEADER}\n")
    while True:
        print("Please choose a level to start!")
        choosing_int = choosing_level()
        print(f"{bcolors.WARNING}You choosed the difficulity {choosing_int}.")
        lives = lives_value(choosing_int)
        print(f"{bcolors.HEADER}You have {lives} lives.")
        CNT_or_CPT = country_or_capital()
        word_line = random_line()
        word_to_guess = choosen_word(CNT_or_CPT,word_line) 
        secret_word = display(word_to_guess)
        print("\n")
        print(f"{bcolors.HEADER}Your word to guess:")
        print(" ".join(secret_word))
        already_tried_letters = []
        while True:
            guess = validate(already_tried_letters)
            secret_word, lives = present(guess, word_to_guess, secret_word, lives)
            print(" ".join(secret_word))
            if not secret_word.__contains__("_") and lives > 0:
                print("\n")
                print(f"{bcolors.OKGREEN} Congratulations! You guessed the word!\n\n\n")
                break
            elif lives == 0:
                print("\n")
                print(f"{bcolors.FAIL} Sorry you lost the game! The word was {word_to_guess}.\n")
                break
        replay = input(f"{bcolors.OKGREEN}Do you want to play again? (Y/n) \n\n\n").upper()
        if replay == "N":
            break

if __name__=="__main__":
    main()
