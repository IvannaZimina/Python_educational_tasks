# In the city XYZ, there is a bank which exchanges only two currencies: euro (€) and dollar ($).
# Write a program which helps the banker do his work well.

# The program has to ask for three inputs:
#   the amount of money before the exchange
#   the name of the currency before the exchange
#   the name of the currency after the exchange

# The program then performs the conversion and outputs the result: the amount of money and the currency name.
# If the banker enters something inappropriate, the program displays an informative message.

# The currency rate for today: 1 € = $1.17 

# Example:
# >> The amount of money to convert? 100.50
# >> Current currency: dollar
# >> Exchange into: euro 
# >> 85.89743589743589

print("The currency rate for today: 1 € = $1.17")

# The currency rate for today: 1 € = $1.17 
EUR_TO_USD = 1.17
USD_TO_EUR = 1 / EUR_TO_USD

# the amount of money before the exchange
amount_str = input(">> The amount of money to convert? ")

try:
    amount = float(amount_str)
except ValueError:
    print(">> .+The currency rate for today: 1 € = \$1\.17.*")
    raise SystemExit()

if amount < 0:
    print(">> Incorrect amount: must be non-negative")
    raise SystemExit()

# the name of the currency before the exchange
src = input(">> Current currency: ").strip().lower()

aliases = {"eur": "euro", "€": "euro", "usd": "dollar", "$": "dollar"}
src = aliases.get(src, src)

# the name of the currency after the exchange
dst = input(">> Exchange into: ").strip().lower()
dst = aliases.get(dst, dst)

# only two currencies: euro (€) and dollar ($)
allowed = {"euro", "dollar"}
if src not in allowed:
    print(">> Unsupported currency: use euro/dollar")
    raise SystemExit()

if dst not in allowed:
    print(">> Unsupported currency: use euro/dollar")
    raise SystemExit()

if src == dst:
    print(">> Source and target currencies must be different")
    raise SystemExit()

if src == "euro" and dst == "dollar":
    result = amount * EUR_TO_USD
elif src == "dollar" and dst == "euro":
    result = amount * USD_TO_EUR
else:
    print(">> Conversion is not available")
    raise SystemExit()

print(">>", result)