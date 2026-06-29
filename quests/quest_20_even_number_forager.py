#!/usr/bin/python3
# This script finds and prints all the even numbers between 1 and 20
for i in range(1, 21):
    # You can use modulo to check if the number number has a remainder when divided by 2
    if i % 2 == 0:
        # Prints the number if it is actually an even number
        print(i)
