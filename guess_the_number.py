import random


def guess(x):
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
    
    

computer_guess(10)

# guess(20)
        