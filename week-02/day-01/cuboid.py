# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000
a = 53.4
b = 11.89
c = 25.5

print("Surface Area: " + str( a*b*2 + a*c*2 + b*c*2))
print("Volume: " + str(a*b*c))
