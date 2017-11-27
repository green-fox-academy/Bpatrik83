# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
#
# Surface Area: 600
# Volume: 1000

a = 10
b = 10
c = 10

volume = int(a * b * c)
surface_area = int(6*a**2)

print("Volume = ", volume)
print("Surface area = ", surface_area)