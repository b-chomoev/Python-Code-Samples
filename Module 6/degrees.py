# Beksultan
# 11/24/2023

# This is a problem #5. This program converts radian to degrees.

import math

user_value = float(input("Enter the angle in radians: "))

conversion = user_value * (180 / math.pi)

degree = math.degrees(conversion)

print(f"User input value in radians: {user_value}")
print(f"Calculated degrees using the formula: {conversion}")
print(f"Calculated degrees using the math module: {degree}")
