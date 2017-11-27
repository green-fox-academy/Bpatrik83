# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

num1 = input("Enter a number: ")
num1 = int(num1)

num2 = input("Enter your tipp: ")
num2 = int(num2)

if num1 == num2:
    print("You found the number: ", num2)
else:
    while num1 != num2:
        if num2 > num1:
            print("The stored number is lower")
        if num2 < num1:
            print("The stored number is higher")
        if num1 != num2:
            num2 = num2 = input("Enter your tipp: ")
            num2 = int(num2)
print("You found the number: ", num2)