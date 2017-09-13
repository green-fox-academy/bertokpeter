# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4
sum_list = []
many = int(input("How many number would you like? "))
while many <= 0:
    many = int(input("Your number should be higher "))
if many > 0:    
    for i in range(many):
        number = int(input("Enter a number "))
        sum_list.append(number)
    Sum = sum(sum_list)
    Average = Sum/many
    print("Sum: " + str(Sum) + ", Avergae:" + str(Average))