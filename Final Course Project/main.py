import time
import random

from choose_your_own_adventure import *
from guess_the_number import guess
from hangman import hangman
from rock_paper_scissors import playrps
from tic_tac_toe import TicTacToe, HumanPlayer, RandomComputerPlayer, play

def introduction():
    print("Welcome to the Beksultan's Adventure Game Club")

def get_player_name():
    return input('What is your name: ')

def play_choose_your_own_adventure():
    print("\nStarting your first level. This level is called 'Choose your own adventure!'")
    choose_path()
    explore_forest()
    crossroad_surprise()
    abandoned_village()
    print("Congratulations! You have passed first level to get your diamond!\n")

def play_guess_the_number():
    print("\nStarting your second level! Try to be careful !")
    guess(10)
    print("Here we GO! One more time !\n")

def play_hangman():
    print("\nThis one is going to be tricky ! Do your best !")
    hangman()
    print("You are awesome !\n")

def play_rock_paper_scissors():
    print("\nThis is a 'Rock, Paper, Scissors' game. Show me your best !")
    print(playrps())
    print("Rock, Paper, Scissors completed!\n")

def play_tic_tac_toe():
    print("\nYou almost there !")
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
    print("Tic Tac Toe completed!\n")

def game_over(name):
    print(f'Congratulations ! You are the hero, and you here is your diamond {name}!')

def main():
    introduction()
    name = get_player_name()

    games = [
       play_choose_your_own_adventure,
       play_guess_the_number,
       play_hangman,
       play_rock_paper_scissors,
       play_tic_tac_toe
    ]

    for game in games:
        if game == introduction:
            game()
        else:
            continue_playing = input("Do you want to continue your journey for a diamond ? (yes/no): ").lower()
            if continue_playing != 'yes':
                break
            game()

    game_over(name)

if __name__ == "__main__":
    main()