# Beksultan
# 11/25/2023

# This is a problem #4 and this program returns True if the year is a leap year.

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year_to_check = 2024
result = is_leap_year(year_to_check)

print(f"{year_to_check} is a leap year: {result}")