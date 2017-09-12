# - Create a function called `factorio`
#   that returns it's input's factorial
input_number = int(input("Please input a number "))
def factorio(number):
    factorial = 1
    for i in range(1, number+1):
        factorial = i*factorial
    return factorial
print(factorio(input_number))