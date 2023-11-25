# Beksultan
# 11/24/2023

# This is a problem #4. This program computes the approximation and then print that value. It should be same as a pi number.

import math

def approximate_pi(number):
    approx_pi = 0

    for i in range(number):
        a = (-1) ** i / (2 * i + 1)
        approx_pi += a

    approx_pi *= 4
    return approx_pi

number = 100000

approximation = approximate_pi(number)

print(f"Approximation of pi using Leibniz formula: {approximation}")
print(f"Value of pi from the math module: {math.pi}")