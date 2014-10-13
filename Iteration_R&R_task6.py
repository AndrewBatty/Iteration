# Andrew Batty
# 13/10/14
# Iteration R&R Task 6

message = input("Please enter a message that you would like to display: ")
repeat = int(input("Please enter the number of times you would like the message to be diplayed beteen 1 and 10: "))
while repeat < 10:
    print("{0}".format(message))
    repeat += 1
    
