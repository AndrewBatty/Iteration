# Andrew Batty
# 21/10/14
# Iteration Revision Exercise 3:

total = 0
average_enter = int(input("Please enter how many numbers you would like to average: "))

for count in range(average_enter):
    number_enter = int(input("Please enter a number: "))
    total = total + number_enter

average = total // average_enter
print("The average of your numbers is {0}".format(average))
