import random

computer_random = random.randrange(1, 101)

print(computer_random)

user_value = int(input('Guess the number: '))

if user_value < computer_random:
    print('Please guess higher')
elif user_value > computer_random:
    print('Please guess lower')
else:
    print('Well done, you guessed it')
