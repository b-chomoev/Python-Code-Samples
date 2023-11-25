# Beksultan
# 11/24/2023

# This problem is #6. This program calculates the factorial of a user.

import math

user_value = int(input('Enter a non-negative integer to calculate its factorial: '))

factorial = 1

for i in range(1, user_value + 1):
    factorial *= i

factorial_math = math.factorial(user_value)

print(f"Calculated factorial using a for statement: {factorial}")
print(f"Calculated factorial using the math module: {factorial_math}")
