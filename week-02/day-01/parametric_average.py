# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4
many = 6
a = [0]*many
for i in range(0,many):
    a[i] = int(input("Enter a number ")) 
Sum = sum(a)
Average = Sum/many
print("Sum: " + str(Sum) + ", Avergae:" + str(Average))