# Write a program that asks the user to enter the number of a month (an integer 1–12) and prints the number of days in that month.
# Implement and use a function - def number_of_days(month: int) -> int
# that takes the month number and returns the number of days.
# For this exercise assume February always has 28 days (no leap-year handling).

# Program behaviour and I/O rules:
#   The program must read exactly one value from standard input (month number).
#   If the input is a valid integer in range 1..12, the program prints only the number of days (an integer) followed by a newline. It may optionally include other text, so tests use regex matching.
#   If the input is not a valid integer or not in the 1..12 range, the program must print an error message containing the phrase Enter a valid month! (case-sensitive as shown) and exit.

def number_of_days(month: int):
    try:
        month_num = int(month)
    except ValueError:
        return None

    if not 1 <= month_num <= 12:
        return None

    if month_num in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month_num == 2:
        return 28
    else:
        return 30

user_input_month = int(input())

result = number_of_days(user_input_month)

if result is None:
    print("Enter a valid month!")
else:
    print(result)