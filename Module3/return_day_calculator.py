# Beksultan
# 11/18/2023

# This program will tell you the number of the of day of the week you will return.

start_day = int(input('Enter your day, where day 0 is Sunday and day 6 is Saturday'))
length_day = int(input('Enter the length of your staying'))

days_in_week = 7

return_day = start_day + length_day

if return_day >= days_in_week:
    return_day -= days_in_week

print("You will return in a day", return_day)
