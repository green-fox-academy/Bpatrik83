# Write a program that asks for two numbers and prints the bigger one

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

if int(num1) > int(num2):
    print(num1)
elif int(num1) < int(num2):
    print(num2)
else:
    print("Equal")