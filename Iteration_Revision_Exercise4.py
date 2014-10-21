# Andrew Batty
# 21/10/14
# Iteration Revision Exercise 4:

valid = False

while not valid:
    number_enter = int(input("Please enter a number between 10 and 20: "))
    if 10 <= number_enter <= 20:
        print("The number you have entered is within range. Thank you.")
        valid = True

