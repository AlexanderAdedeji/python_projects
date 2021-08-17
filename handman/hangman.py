import random
import string
from words import words




def generate_valid_word(words):
    generated_word = random.choice(words)
    while '-' in generated_word or ' ' in generated_word:
        generated_word = random.choice(words)
    
    return generated_word



def hangman():
    word = generate_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print('You have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        # word_list = []
        # for letter in word:
        #     if letter in used_letters:
        #         print(letter)
        #     else:j
        
        #         print('_')    
        print('Current Word: ', ' '.join(word_list))
        
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
            
        else:
            print('Invalid character. Please try again. ')
    
    print('Hey, Congratulations, You Won!!')
            

    
    
hangman()