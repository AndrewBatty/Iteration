# Andrew Batty
# 29/10/14
# Development exercise 4

print("This program will ask you to input a series of numbers. When you are finished please enter -1, to end the program.")

series = 0
max_num = 0

while series >= 0:
    series = int(input("Please enter a number: "))
    if series > max_num:
        max_num = series
if series == -1:
    print("The largest integer in the series is {0}".format(max_num))
    

