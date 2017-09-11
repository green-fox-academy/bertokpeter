# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
d = int(input("Fourth number: "))
e = int(input("Fifth number: "))
Sum = a+b+c+d+e
Average = Sum/5
print("Sum: " + str(Sum) + ", Average: " + str(Average))