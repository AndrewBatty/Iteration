# Andrew Batty
# 29/10/14
# Development exercise 1

n = int(input("Please enter a number: "))
total = 1
n = n + 1

for count in range(1,n):
    total = total * count
    
print("The total of your factorial is {0}".format(total))

    
