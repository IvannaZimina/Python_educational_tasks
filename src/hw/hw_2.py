# Write a program that asks the user to enter the number of a month.
# The program has to output the number of days in that month.
# Also make sure if the user inputs anything ridiculous, the program has to give a corresponding feedback about it.
# Use try-except.

# Test your program with different inputs and make sure the program works correctly.
# For example: -100, 0, 1, 2, 5, 9, 10, 12, 13, 100, blabla

# Here are some examples of the program output.
 
#  Enter the number of a month: blabla
#  Please enter a number

#  Enter the number of a month: 0
#  The number of a month must be in the range [1-12]

#  Enter the number of a month: 12
#  That month has 31 days in it.

#  Enter the number of a month: 4
#  That month has 30 days in it.

#  Enter the number of a month: 2
#  That month has 28 or 29 days in it.

user_input = input("Enter the number of a month: ")

try:
    month = int(user_input)
except ValueError:
    print("Please enter a number")
    exit()
    
if month < 1 or month > 12:
    print("The number of a month must be in the range [1-12]")
    exit()
    
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("That month has 31 days in it.")
elif month in [4, 6, 9, 11]:
    print("That month has 30 days in it.")
elif month == 2:
    print("That month has 28 or 29 days in it.")
    
