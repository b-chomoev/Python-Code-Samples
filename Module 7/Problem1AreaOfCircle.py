# Beksultan
# 11/25/2023

# This is problem #1 and this program finds area of a cirlce.

import math

def areaOfCircle(r):
    area = math.pi * (r ** 2)
    return area

radius = int(input('Enter your radius: '))

result = areaOfCircle(radius)

print(f"The area of the circle with radius {radius} is: {result}")
