
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


def lives_value(choosing_int):
    lives = 0
    if choosing_int == 1:
        lives = 8
            #import smaller word
    elif choosing_int == 2:
        lives = 6
            #import longer word
    else:
        lives = 4
            #import longest word
    return lives


def country_or_capital():
    country_or_capital = input("Choose from countries or capitals with 'CNT' or 'CPT': ").upper()
    while True:
        if country_or_capital == 'CNT':
            return 0
        elif country_or_capital == 'CPT':
            return 1
        else:
            country_or_capital = input("Choose from 'CNT' or 'CPT'")

import random

def random_line():
    f = open("countries-and-capitals.txt", "r")
    file_content = f.read()
    word_list = file_content.split('\n')
    word_line = random.choice(word_list)
    return word_line.upper()

def choosen_word (CNT_or_CPT, word_line):
    word_line_split = word_line.split('|')
    if CNT_or_CPT == 0:
        return word_line_split[0]
    else:
        return word_line_split[1]

def display(word_to_guess):
    secret_word = ""
    for i in word_to_guess:
        if i == " ":
            secret_word += " "
        else:
            secret_word += "_"
    return secret_word

def validate(already_tried_letters):
        guess_letter = input("Please guess a letter or word: ").upper()
        while True:
            if guess_letter in already_tried_letters:
                print("You already guessed this letter!")
                guess_letter = input("Try an other one: ")
            else:
                already_tried_letters.append(guess_letter)
                return guess_letter

def present(guess, word_to_guess, secret_word:str, lives):
    hangman = (

"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H""",

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    HA""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN""")
    new_secret_word = []
    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                new_secret_word.append(guess)
            else:
                new_secret_word.append(secret_word[i])
        secret_word = ("".join(new_secret_word))
        return secret_word, lives
    else:
        lives -= 1
        print("Lives ", lives)
        print(hangman[7 - lives])
    return secret_word, lives

# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4

def main():
    print("\n" * 5)
    print("Hello to our Hangman Game!\n")
    while True:
        print("Please choose a level to start!")
        choosing_int = choosing_level()
        print(f"You choosed the difficulity {choosing_int}.")
        lives = lives_value(choosing_int)
        print(f"You have {lives} lives.")
        CNT_or_CPT = country_or_capital()
        word_line = random_line()
        print(word_line)
        word_to_guess = choosen_word(CNT_or_CPT,word_line)
        print(f"The choosen word is {word_to_guess}") 
        secret_word = display(word_to_guess)
        print("Your word to guess:")
        print(secret_word)
        already_tried_letters = []
        while True:
            guess = validate(already_tried_letters)
            print(guess)
            secret_word, lives = present(guess, word_to_guess, secret_word, lives)
            print(secret_word)
            if not secret_word.__contains__("_") and lives > 0:
                print("\n Congratulations! You guessed the word!\n\n\n")
                break
            elif lives == 0:
                print("\n Sorry you lost the game!\n\n\n")
                break
        replay = input("Do you want to play again? (Y/N) \n\n\n").upper()
        if replay == "N":
            break

if __name__=="__main__":
    main()
