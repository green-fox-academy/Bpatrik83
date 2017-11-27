# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

num = input("Enter a number: ")
num = int(num)
str = "*"

for i in range(num):
    print(str)
    str += "*"