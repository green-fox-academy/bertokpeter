# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %   %
# %   %
# %   %
# %   %
# %%%%%
#
# The square should have as many lines as the number was
a = int(input("Please enter a number: "))
for i in range(1,(a+1)):
    if i==1 or i == a:
        print("%"*(a-1))
    else:
        print("%"+" "*(a-3)+"%")