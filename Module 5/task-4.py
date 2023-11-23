# Beksultan
# 11/22/2023

# This program iterates the integers from 1 to 50 and telling you its division.

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print('Divisible by both')
    elif num % 3 == 0:
        print('Divisible by three')
    elif num % 5 == 0:
        print('Divisible by five')
    else:
        print(num)
