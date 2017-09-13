# Write a program that reads a number form the standard input,
# If the number is zero or smaller it should print: Not enough
# If the number is one it should print: One
# If the number is two it should print: Two
# If the number is more than two it should print: A lot
a = int(input("Please write a number here: "))
if a <= 0:
    print("Not enough")
elif a == 1:
    print("One")
elif a == 2:
    print("Two")
else:
    print("A lot")