# - Write a function called `sum` that sum all the numbers
#   until the given parameter
input_number = int(input("Please input a number "))
def sum_(number):
    number_list= list(range(1,number+1))
    return sum(number_list)
print(sum_(input_number))