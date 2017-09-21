# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.
try:
    def adder(number):
        if number == 1:
            return 1 
        elif number > 1:
            return number + adder(number-1)
        else:
            return number + adder(number+1)
    print(adder(9))
except RecursionError:
    print("number must be integer not float")