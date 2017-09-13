# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
#Solution 1
def list_checker(numbers):
    if 4 in numbers and 8 in numbers and 12 in numbers and 16 in numbers:
        print(True)
    else:
        print(False)
list_checker(list_of_numbers)
#Solution 2
def checker(numbers):
    elements = [4, 8, 12, 16]
    checker = []
    for i in elements:
        if i in numbers:
            checker.append(1)
    if sum(checker) == 4:
        print(True)
    else:
        print(False)
checker(list_of_numbers)