# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
def powerN(base, power):
    if base < 1 or power < 1:
        return "base or power must be higher or equal to 1"
    if power == 1:
        return base
    else:
        return base * powerN(base,power-1)

print(powerN(2.6,7))