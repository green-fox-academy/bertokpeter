# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was
a = int(input("Please enter a number: "))

for i in range(1,(a+1)//2+1):
    print(" "*((a+1)//2-i)+"*"*(i*2-1)+" "*((a+1)//2-i))
if a%2 != 0:   
    for i in range(1,a//2+1):
        print(" "*i+"*"*(a-i*2)+" "*i)
else:   
    for i in range(1,a//2+1):
        print(" "*(i-1)+"*"*((a+1)-i*2)+" "*(i-1))