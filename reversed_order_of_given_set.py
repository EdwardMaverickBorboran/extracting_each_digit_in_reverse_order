# Create a program that will --

# Extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

# DEADLINE: JANUARY 26, 2024

# pseudocode

# Given set of numbers
set_number = int(input("Enter a list of numbers:"))
print("The set of number is:", set_number)

# Setting up a variable and converting the given set of numbers to string
set_number_str = str(set_number)[::-1]

# Displaying the output
print("Reversed order of the set:", " ".join(set_number_str))