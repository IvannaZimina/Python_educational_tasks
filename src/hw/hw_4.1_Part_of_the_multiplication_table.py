# Write a program that:
#   Prompts the user to enter one integer.
#   Multiplies the entered number by integers from 1 to 9.
#   Prints each multiplication in the following format: number * i = result

# Each result must be printed on a new line.
# Input - One integer.

# Output - Exactly 9 lines in this format:
#   n * 1 = ...
#   n * 2 = ...
#   ...
#   n * 9 = ...

# If the input is not a valid integer, print: Enter a valid number!
# No extra blank lines are allowed.

try:
    number = int(input())

    for i in range(10):
        result = number * i
        print(f"{number} * {i} = {result}")    
    
except ValueError:
    print("Enter a valid number!")
