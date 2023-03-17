import random

while True:
    user = input('Enter a choice (rock, paper, scissors): ')
    possible_actions = ["rock","paper","scissors"]
    computer = random.choice(possible_actions)
    print(f'\nYou chose {user}, computer chose {computer}.\n')

    if user == computer:
        print(f'Both player selected chose {user}. It is a TIE!')
    elif user == 'rock':
        if computer == 'scissors':
            print('Rock smashes scissors! You WIN')
        else:
            print('Paper covers rock! You LOSE.')
    elif user == 'paper':
        if computer == 'rock':
            print('Paper covers rock! You WIN.')
        elif computer == 'scissors':
            print('Scissors cuts paper. You LOSE.')
    elif user == 'scissors':
        if computer == 'paper':
            print('Scissors cuts paper. You WIN.')
        elif computer == 'rock':
            print('Rock smashes scissors! You LOSE')

    play_again = input('Play again? (y/n): ')
    if play_again.lower() != 'y':
        break
