# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

def bunny_ears(num_of_bunnys):
    if not num_of_bunnys%1 == 0:
        return "Don't slice up the bunnies!"
    elif num_of_bunnys < 0:
        return 0
    elif num_of_bunnys == 1:
        return 2
    else:
        return 2 + bunny_ears(num_of_bunnys-1)

print(bunny_ears(35.5))
