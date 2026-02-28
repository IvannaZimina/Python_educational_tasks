#========== TASK =======================================================================================
# Write a program that computes the difference between the total amount paid on an installment plan and the initial (cash) price of a product. Implement and use a function:
#   def price_difference(initial_price: float, monthly_payment: float, months: int) -> float
#   that returns (monthly_payment * months) - initial_price.

# Program behaviour and I/O rules:
#   The program must read three values from standard input in this order, each on its own line:
#       initial price (a number; integer or float)
#       monthly payment (a number; integer or float)
#       number of months (an integer)
#   If the inputs are valid numeric values (and months can be parsed as integer), the program prints the numeric difference (which can be negative, zero or positive). Tests will match with a regex allowing any surrounding text.
#   If any input is not parseable as the expected number (e.g., non-numeric strings), the program must print an error message containing the phrase Enter valid numbers! (case-sensitive as shown) and exit.


def price_difference(initial_price: float, monthly_payment: float, months: int) -> float:
    return (monthly_payment * months) - initial_price

try:
    initial_price = float(input())
    monthly_payment = float(input())
    months = int(input())
    
    difference = price_difference(initial_price, monthly_payment, months)
    print(int(difference))
except ValueError:
    print("Enter valid numbers!")

