# Find the part of int

#    Create a function that takes a number and a list of numbers as a parameter
#    Returns the indeces of the numbers in the list where the first number is part of
#    Returns an empty list if the number is not part any of the numbers in the list

# Example

#    input: [1, 11, 34, 52, 61], 1
#    output: [0, 1, 4]

input_list = [1, 11, 34, 52, 61]
n = 1
output_list = []

def listIndex(input_list, n):
    for i in range(len(input_list)):
        if str(n) in str(input_list[i]):
            output_list.append(i)

    return output_list

print(listIndex(input_list, n))

