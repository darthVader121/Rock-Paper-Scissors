import random

def play():
    user = input("What's your choice ? 'r' for rock, 'p' for papers, 's' for scissors \n")
    computer = random.choice(['r','p','s'])
    print(user,computer)

    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user,computer):
        return 'You Won!'
    return 'You Lost!'

def is_win(player,opponent):
    #returns true if player is wining
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

print(play())

