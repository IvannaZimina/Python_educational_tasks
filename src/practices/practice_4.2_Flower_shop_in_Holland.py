# In a Dutch flower shop, flowers are given according to this rule:
#    1st customer → 1 flower
#   2nd customer → 0 flowers
#   3rd customer → 3 flowers
#   4th customer → 0 flowers
#   5th customer → 5 flowers etc.

# Only customers with odd positions receive flowers equal to their position number.

# Write a program that:
#   Prompts the user to enter the number of customers (non-negative integer).
#   Calculates the total number of flowers given away using a loop.
#   Prints the result.

# Input rules - One non-negative integer.
# Output format - # You will need to give away X flowers.
# If input is invalid, print: Enter a valid number!

customer_count = input()

try:
    n = int(customer_count)
    if n < 0:
        print("Enter a valid number!")
    else:
        total_flowers = 0
        
        for i in range(1, n + 1, 2):
            total_flowers += i
            
        print(f"You will need to give away {total_flowers} flowers.")
        
except ValueError:
    print("Enter a valid number!")