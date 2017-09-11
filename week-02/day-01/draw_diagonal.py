# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was
a = int(input("Please enter a number: "))
for i in range(1,a+1):
    if i == 1:
        print("%"*(a-1))
    elif i < a-1:
        print("%"+" "*(i-2)+"%"+" "*(a-2-i)+"%")
    elif i < a:
        print("%"+" "*(a-3)+"%")
    else:
        print("%"*(a-1))