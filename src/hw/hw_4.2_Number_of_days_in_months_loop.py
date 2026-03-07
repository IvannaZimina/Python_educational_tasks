# Update the previous "Number of days in months" program so that:
#   The program repeatedly asks the user for a month number.
#   The loop continues until the user enters the word: done

# For valid month numbers (1–12), print: The number of days in this month is X

# If the user enters:
#   A non-numeric value → print: Please enter a number
#   A number outside 1–12 → print: The number of month must be in the range 1-12
#   February is always 28 days.

# Important:
#   No extra blank lines.
#   No newline after final output.
#   Stop immediately when user enters done.

def number_of_days(month: str):
    try:
        month_num = int(month)
    except ValueError:
        print("Please enter a number")
        return None

    if not 1 <= month_num <= 12:
        print("The number of month must be in the range 1-12")
        return None

    if month_num in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month_num == 2:
        return 28
    else:
        return 30


#The loop continues until the user enters the word: done
while True:
    # The program repeatedly asks the user for a month number.
    user_input_month = input()

    if user_input_month == "done":
        break  # Stop immediately with no output

    days = number_of_days(user_input_month)

    if days is not None:
        print(f"The number of days in this month is {days}")

