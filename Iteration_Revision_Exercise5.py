# Andrew Batty
# 21/10/14
# Iteration Revision Exercise 5:

print("This program will ask you for a series of numbers then average them. When you have finished entering your numbers please enter -1 last.")

total = 0
num_ent = 0
count = 0

while num_ent >= 0:
    num_ent = int(input("Please enter an number: "))
    if num_ent >= 0:
        total = total + num_ent
        count = count + 1

average = total // count

print("The average of the numbers you have entered is {0}".format(average))
      
