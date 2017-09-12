# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was
a = int(input("Please enter a number: "))
for i in range(1,a+1):
    print(" "*(a-i) + "*"*(i*2-1))