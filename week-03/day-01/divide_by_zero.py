# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0
divisor = int(input("Enter your number here: "))
def division(number):
    try:
        print(10/number)
    except ZeroDivisionError:
        print("fail")
division(divisor)