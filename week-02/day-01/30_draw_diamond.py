# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

num = int(input("Enter a number: "))

while num % 2 == 0:
    num = int(input("Enter an odd number: "))

str = "*" * num * 2
j = 1
odd_even = 0

if num % 2 == 0:
    odd_even = 1

for i in range(num // 2 - odd_even):
    print(num * " ", str[0:j])
    num -= 1
    j += 2

for k in range(num - odd_even):
    print(num * " ", str[0:j])
    num += 1
    j -= 2


