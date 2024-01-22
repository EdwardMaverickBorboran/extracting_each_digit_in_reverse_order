# Create a program that will --

# Extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

# DEADLINE: JANUARY 26, 2024

# pseudocode

# Given set of numbers
set_number = 7563
print("The set of number is:", set_number)

# Setting up a variable and convert the given set of numbers to str
set_number_str = str(set_number)[::-1]

# Displaying the output
print("Reversed order of the set:", set_number_str)