# Beksultan
# 12/2/2023

# This program pushes numbers into the array that are divisible by 10.

array = []

counter = 0

while counter <= 50:

    if counter % 10 == 0:

        array.append(counter)

    counter += 1

print("List of values divisible by 10:", array)
