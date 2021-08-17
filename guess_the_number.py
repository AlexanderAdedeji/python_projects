import random


def user_guess(x):
    random_number = random.randint(1,x)    
    guess = 0   
    while guess != random_number:
        guess = int(input(f'Guess a random number between 1 and {x}: '))
        if guess < random_number:
            print('Too bad, try again, number was too low')
        elif guess >  random_number:
            print('Too bad , guess again, number was too high')
    print(f'Congratulations, You have guess the number {random_number} correctly')
        


def computer_guess(x):
    low =1
    high = x
    feedback =''
    while feedback != 'c' and low != high:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high
        feedback = input(f'Is {guess} too high (H), too low(L), or Correct (C)')
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay!, The Computer Guessed Your Number {guess} correctly')
    
    



def play():
    print('Welcome, this is a guessing game, where either you or the computer thinks of a secret number and the other player tries to guess what it is')
    decision = ''
    choices = ['i', 'c']
    while decision not in choices:
        decision = input("Enter 'i' if you want the computer to guess your secret number or 'c' if you want the computer to guess ")
    if decision== 'i':
        computer_guess(100)
    elif decision =='c':
        x = input('Great, the computer already has a secret number, now take a guess')
        user_guess(x)
        
    
        






play()

        