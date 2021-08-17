import random


def check_winner(player_1, player_2):
    if player_1 == player_2:
        return "it's a tie"
    if (player_1 == 'p' and player_2=='r') or (player_1 =='r' and player_2 =='s') or (player_1 == 's' and player_2 == 'p'):
        return "Hey, Congratulations, You Won!!"
    return 'You Lost!' 
    

def play_game(): 
    choices= ['r', 's', 'p']
    computer_choice = random.choice(choices)
    user_choice=''
    while user_choice not in choices:
        print(f'{user_choice} is not in the option, try again')
        user_choice =input("Pick a choice between : 'r' for Rock, 'p' for Paper and 's' for Scissors : ")        

    results =check_winner(user_choice, computer_choice)   
    print(results)


play_game()