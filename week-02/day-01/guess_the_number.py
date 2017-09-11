# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8
import random
number = random.randint(1,101)
a = int(input("Can you guess the number? "))
while a != number:
    print("Guess again... ")
    if a < number:
        print("The stored number is higher")
        a = int(input("Can you guess the number? "))
    else:
        print("The stored number is lower")
        a = int(input("Can you guess the number? "))
if a == number:
    print("You found the number: " + str(number))