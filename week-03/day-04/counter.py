# Write a recursive function that takes one parameter: n and counts down from n.
try:
    def counter(number):
        if number == 0:
            return 0
        else:
            return str(number) + " " + str(counter(number-1))

    print(counter(100))
except RecursionError:
    print("number must be integer and positive")