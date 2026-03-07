# An optimal distance between the TV-set screen and the eyes of the user is about 2.5 times larger than the diagonal of the TV screen.
# For example, if the distance from the screen to the chair is known,
# the optimal diagonal of the screen can be calculated as follows:
#       screen_diagonal_in_inches = distance_in_meters * 100 * 0.39 / 2.5

# Create a function screen_diagonal
#   with one parameter for the distance between the screen and the eyes;
#   the function calculates the optimal diagonal of the screen in inches;
#   the function returns the result as rounded integer number.

# The returned value must be rounded to the whole part and converted to integer.
# The conversion must be done in the function (use round, then int)

# Next, use the function in your program:
#   the distance from the screen to the eyes is asked from the user;
#   the diagonal of the screen is printed out.

# Important! Make your program so that the function itself doesn't prompt the user and doesn't print out anything. 
# This functionality must be implemented outside the function. The function is responsible only for the calculations.

# Example 1
# >>> Enter the distance from the screen in meters: 6.5
# >>> Screen diagonal should be 101 inches long.

# Example 2
# >>> Enter the distance from the screen in meters: large
# >>> Enter a valid distance!

def screen_diagonal(distance_in_meters: float):
    try:
        # Input is always a string, that's why we bring to format float()
        distance = float(distance_in_meters)
    except ValueError:
        return None

    diagonal = distance * 100 * 0.39 / 2.5

    return int(round(diagonal))

# Calculations and outputs

distance_in_meters = float(input('Enter the distance from the screen in meters: '))
result = screen_diagonal(distance_in_meters)

if result is None:
     print("Enter a valid distance!")
else:
    print(f"Screen diagonal should be {result} inches long.")
