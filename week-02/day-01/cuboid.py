# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000
a = 53
b = 11
c = 25

print("Surface Area: " + str( 2*(a*b + a*c + b*c)))
print("Volume: " + str(a*b*c))