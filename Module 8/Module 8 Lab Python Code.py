# Beksultan
# 11/26/2023

# This is a problem #5 and this program checks whether your game character has picked up all the items needed
# to perform certain tasks and checks against any status debuffs

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses

def check_task_completion(character):
    tasks ={
        'Climb mountain': {'items' : ['rope', 'coat', 'first aid kit'], 'debuff': 'slow'},
        'Cook a meal': {'items': ['pan', 'groceries'], 'debuff': 'small'},
        'Write a book': {'items': ['pen', 'paper', 'idea'], 'debuff': 'confusion'}
    }

    for task, requirements in tasks.items():
        items_needed = requirements['items']
        debuff_not_allowed = requirements['debuff']

        if all(item in character.weapons for item in items_needed):
            if debuff_not_allowed not in character.weaknesses:
                print(f"Task '{task}' is complete!")
            else:
                print(f"Cannot complete task '{task}' due to debuff: {debuff_not_allowed}")
        else:
            print(f"Cannot complete task '{task}' due to missing items: {items_needed}")

player1 = character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])
player1.profile()

for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

check_task_completion(player1)
