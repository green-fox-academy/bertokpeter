# Find the part of int

# Create a function that takes a number and a list of numbers as a parameter
# Returns the indeces of the numbers in the list where the first number is part of
# Returns an empty list if the number is not part any of the numbers in the list
# Example

input_list= [1, 11, 34, 52, 61]
input_number = 1
# output: [0, 1, 4]
def find_integer(number_list, number):
    if number in number_list:
        return enumerate(number)
    else:
        return []
print(find_integer(input_list,input_number))