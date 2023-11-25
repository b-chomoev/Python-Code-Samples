# Beksultan
# 11/25/2023

# This is a Problem #2 and this program check a number in a given range.

def checkRange(number):
    if number in range(1, 10):
        print("Your number is in range")
    else:
        print("Your number is not in range")

user_value = int(input("Enter a number: "))

checkRange(user_value)
