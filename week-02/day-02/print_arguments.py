# - Create a function called `printer`
#   which prints the input parameters
#   (can have multiple number of arguments)
input_string01 = input("Please input something ")
input_string02 = input("Please input something again ")
def printer(input, parameter):
    print(input + " " + parameter)
printer(input_string01,  input_string02)