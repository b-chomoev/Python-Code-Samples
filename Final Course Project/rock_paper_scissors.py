import random

def playrps():
    lives = 6
    wins = 0

    while lives > 0 and wins < 5:
        user = input("What's your choice ? 'r' for rock, 'p' for paper and 's' for scissors\n You have to win 5 times "
                     "in order to move forward !")
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            print("It's a tie")
        elif is_win(user, computer):
            print('You won!')
            wins += 1
        else:
            print('You lost!')
            lives -= 1

        print(f"Lives: {lives}, Wins: {wins}")

    if wins == 5:
        return 'Congratulations! You won the game!'
    else:
        return 'Sorry, you ran out of lives. Game over.'

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')