# Beksultan
# 11/26/2023

# This is a problem #2 and this program takes two inputs and compares it to 10

def compare_values():

    user_value1 = int(input('Enter your first value: '))
    user_value2 = int(input('Enter your second value: '))

    result = user_value2 + user_value1

    if result == 10:
        print('Value is equal to 10')
    elif result > 10:
        print("The sum is greater than 10")
    else:
        print('The sum is less than 10')

compare_values()