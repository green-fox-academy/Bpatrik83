# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

var1, var2, var3, var4, var5 = input("Enter five numbers: ").split()

sum = int(var1) + int(var2) + int(var3) + int(var4) + int(var5)

print("Sum: ", sum)
print("Average: ", sum / 5)