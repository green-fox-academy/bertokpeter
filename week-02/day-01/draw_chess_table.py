# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#
a = int(input("Please enter a number: "))
while a <= 0:
    a = int(input("Please enter a bigger number: "))
if a > 0:
    if a == 1:
        print("%")
    elif a%2 == 0:
        for i in range(1,a+1):
            if i%2 == 1:
                print(("%"+" ")*(a//2))
            else:
                print((" "+"%")*(a//2))
    else:
        for i in range(1,a+1):
            if i%2 == 1:
                print(("%"+" ")*(a//2)+"%")
            else:
                print((" "+"%")*(a//2)+" ")