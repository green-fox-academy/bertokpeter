# - Create an array variable named `ag`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Double all the values in the array
ag = list(range(3,8))
for i in range(len(ag)):
    ag[i] *= 2
print(ag)