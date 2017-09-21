# Given a non-negative int n, return the sum of its digits recursively (no loops). 
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while 
# divide (/) by 10 removes the rightmost digit (126 // 10 is 12).

try:
    def sum_digits(number):
        if number < 0:
            return "number must be positive"
        else:    
            log10 = len(str(number))-1
            if len(str(number)) == 1:
                return number
            else:
                return number//(10**log10) + sum_digits(number%(10**log10))

    print(sum_digits(9856.26))
except RecursionError:
    print("number must be integer not float")

def sum_digits_ati(number):
    if number == 0:
        return number
    else:
        return number%10 + sum_digits(number//10)

print(sum_digits_ati(333)) 