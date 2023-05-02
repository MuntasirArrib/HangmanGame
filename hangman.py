import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word: 
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #A variable that saves all the letters in a word as a set-how to keep track of the guessed word
    alphabet = set(string.ascii_uppercase) #predetermined list of uppercase characters in the english dictionary
    used_letters = set() # what the user has guessed
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f'You have {lives} lives left')
        user_letter = input('Guess a letter: ').upper()     #Getting user input
        if user_letter in alphabet - used_letters: #if the letter is in a alphabet and havent been used yet
            used_letters.add(user_letter)
            if user_letter in word_letters:  
                word_letters.remove(user_letter)
            else: 
                lives = lives - 1
        
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
            lives = lives - 1
        
        else: 
            print('Invalid character. Please try again! ')
            lives = lives - 1
            
        print('You have used these letters: ', ' '.join(used_letters))
        word_list = [x if x in used_letters else '-' for x in word] #did not understand
        print('Current word: ', ' '.join(word_list))
    if lives == 0:
        print(f"Sorry you died. The word was {word}")
    else: 
        print("Congrats you did it!")

hangman()



