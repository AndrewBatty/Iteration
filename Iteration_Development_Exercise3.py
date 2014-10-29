# Andrew Batty
# 29/10/14
# Development exercise 3

message = str(input("please enter you would liked displayed backwards: "))
message = message[::-1]
length = len(message)

for index in range(length):
    print(message[index])
