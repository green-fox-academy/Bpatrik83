# Find the substring in the list

#    Create a function that takes a string and a list of string as a parameter
#    Returns the index of the string in the list where the first string is part of
#    Returns -1 if the string is not part any of the strings in the list

# Example

#    input: "ching", ["this", "is", "what", "I'm", "searching", "in"]
#    output: 4

input_list = ["this", "is", "what", "I'm", "searching", "in"]
n = "ching"
output_list = []

def listIndex(input_list, n):
    for i in range(len(input_list)):
        if n in input_list[i]:
            return i

    return -1

print(listIndex(input_list, n))
