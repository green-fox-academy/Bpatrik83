# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

test_number = input("Enter a test case number: ")
test_number = int(test_number)
result = 0

for i in range(test_number):
    sum = input("Enter number: ")
    result += int(sum)

print("Sum : ", result)
print("Average: ", result / test_number)