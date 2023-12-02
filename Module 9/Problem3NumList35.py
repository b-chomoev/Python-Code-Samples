# Beksultan
# 12/2/2023

# This program summarize the array of numbers until the sum reaches 100

numbers = []

sum = 0

while sum <= 100:
    user_value = int(input('Enter your number: '))
    numbers.append(user_value)
    sum += user_value

print("List of numbers:", numbers)
print("Sum of numbers:", sum)
