def price_difference(initial_price: float, monthly_payment: float, months: int) -> float:
    return (monthly_payment * months) - initial_price

def better_plan(initial_price: float, m1: float, n1: int, m2: float, n2: int) -> int:
    diff1 = price_difference(initial_price, m1, n1)
    diff2 = price_difference(initial_price, m2, n2)

    if diff1 < diff2:
        return 1
    elif diff2 < diff1:
        return 2
    else:
        return 0

def main():
    try:
        initial_price = float(input())
    except ValueError:
        print("Enter a valid price!")
        return
    
    try:
        m1 = float(input())
        n1 = int(input())
        m2 = float(input())
        n2 = int(input())
    except ValueError:
        print("Enter valid numbers!")
        return

    result = better_plan(initial_price, m1, n1, m2, n2)

    if result == 1:
        print("The first installment plan is better!")
    elif result == 2:
        print("The second installment plan is better!")
    else:
        print("Both installment plans cost the same.")

main()

#========== TASK =======================================================================================
# Write an interactive program that asks the user for the initial price of a product and for two different installment plans, compares them and prints which plan is better for the customer.

# Requirements and functions:
#   Reuse the price_difference function from Task 2 (or implement the same logic).
#   The price difference is defined as (monthly_payment * months) - initial_price.
#   A smaller price difference is better for the customer (less extra paid).
#    Implement a helper function: def better_plan(initial_price: float, m1: float, n1: int, m2: float, n2: int) -> int
#    that returns:
#       1 if the first plan is better (diff1 < diff2),
#       2 if the second plan is better (diff2 < diff1),
#       0 if both plans cost the same (diff1 == diff2).

# Interactive I/O specification:
#    The program must read five values from standard input, each on its own line, in this order:
#       initial price (number)
#       monthly payment of first plan (number)
#       number of months of first plan (integer)
#       monthly payment of second plan (number)
#       number of months of second plan (integer)
#    After computing, the program must print one of the following exact phrases somewhere in its output (tests use regex matching):
#       The first installment plan is better!
#       The second installment plan is better!
#       Both installment plans cost the same.

#    If any of the numeric inputs cannot be parsed (for example the price is a non-numeric string),
#    the program must print an error message containing the phrase Enter a valid price! (for invalid initial price) or
#    Enter valid numbers! (if other fields are non-numeric).
#    For the test cases below we use Enter a valid price! when the initial price is invalid.