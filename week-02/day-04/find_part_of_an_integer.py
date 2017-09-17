# Find the part of int

# Create a function that takes a number and a list of numbers as a parameter
# Returns the indeces of the numbers in the list where the first number is part of
# Returns an empty list if the number is not part any of the numbers in the list
# Example

input_list= [1, 11, 34, 52, 61, 315]
input_number = 1
# output: [0, 1, 4]
def find_integer(number_list, number):
    string_number = str(number)
    output = []
    for i in range(len(number_list)):
        list_number = str(number_list[i])
        if string_number in list_number:
            output.append(i)
    return output
print(find_integer(input_list,input_number))