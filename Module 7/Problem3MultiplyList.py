# Beksultan
# 11/25/2023

# This is a problem #3 and this program mupltiplies all numbers in array.

def multiplyList(number):
    result = 1
    for i in number:
        result *= i
    return result

number_list = [5, 2, 7, -1]
result = multiplyList(number_list)

print(result)
