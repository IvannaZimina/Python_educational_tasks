# Mantra is a word or sound that is repeated as a prayer or to help people meditate. Mantra is repeated as many times as it as necessary.

# Write a program that:
#   Prompts the user to enter a sentence (the mantra).
#   Prompts the user to enter how many times the mantra should be repeated (a non-negative integer).
#   Prints the mantra exactly that many times, each on a new line.

# Input rules
#   First line: mantra (string)
#   Second line: number of repetitions (non-negative integer)

# Output rules
#   Print the mantra repeated the specified number of times.
#   If the number of repetitions is not a valid non-negative integer, print:
# Enter a valid number!

mantra = input()
repetitions = input()

try:
    count = int(repetitions)
    if count < 0:
        print("Enter a valid number!")
    else:
        for _ in range(count):
            print(mantra)
except ValueError:
    print("Enter a valid number!")