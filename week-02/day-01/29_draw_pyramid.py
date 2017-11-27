# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

num = input("Enter a number: ")
num = int(num)
str = "*"

for i in range(num):
    print(num * " " + str)
    str += "*" * 2
    num -= 1

