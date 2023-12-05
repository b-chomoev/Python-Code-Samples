import time
import random

def introduction():
    print("Welcome to the Ultimate Adventure Game!")

def get_player_name():
    return input('Type your name: ')

def choose_path():
    return input('You find yourself at a crossroad. To the left is a mysterious forest, '
                 'and to the right is a dark cave. Which path will you take? (forest/cave)').lower()

def explore_forest():
    print('As you enter the mysterious forest, you encounter a talking owl.')

    owl_question = input('The owl asks you a riddle: "What has keys but can\'t open locks?" '
                         'Do you know the answer? (yes/no)').lower()

    if owl_question == 'yes':
        print('The owl is impressed! It guides you safely through the forest.')
    else:
        print('The owl hoots sadly, and you get lost in the enchanted forest. You lose.')

def enter_cave():
    print('You enter the dark cave and discover a treasure chest.')

    chest_choice = input('Do you want to open the chest? It might be trapped! (open/leave)').lower()

    if chest_choice == 'open':
        trap_result = random.choice([True, False])

        if trap_result:
            print('The chest was trapped! You triggered a trap and lose the game.')
        else:
            print('Congratulations! You found a magic amulet in the chest. You WIN!')
    else:
        print('You decide not to open the chest and continue your journey.')

def crossroad_surprise():
    print('At the crossroad, a mysterious figure appears and offers you a magical map.')

    map_choice = input('Do you accept the magical map? (yes/no)').lower()

    if map_choice == 'yes':
        print('The map leads you to a hidden shortcut. You successfully navigate through the journey. You WIN!')
    else:
        print('You decline the magical map. The journey continues with its challenges.')

def abandoned_village():
    print('You come across an abandoned village.')

    explore_choice = input('Do you want to explore the village? (explore/ignore)').lower()

    if explore_choice == 'explore':
        print('While exploring, you find valuable artifacts. You gain extra points! You WIN!')
    else:
        print('You decide to ignore the village, and the journey continues.')

def game_over(name):
    print(f'Thank you for playing, {name}!')

def main():
    introduction()
    name = get_player_name()

    path_choice = choose_path()

    if path_choice == 'forest':
        explore_forest()

    elif path_choice == 'cave':
        enter_cave()

    else:
        print('Not a valid option. You lose!')

    crossroad_surprise()

    abandoned_village()

    game_over(name)

if __name__ == "__main__":
    main()