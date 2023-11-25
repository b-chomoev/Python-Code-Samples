# Beksultan
# 11/25/2023

# This is a Problem #4 and this program returns a new list from the array.

def uniqueElements(numbers):
    unique_list = []

    for i in numbers:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

array = [1, 3, 3, 3, 6, 2, 3, 5]

result = uniqueElements(array)

print(result)