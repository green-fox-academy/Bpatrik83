# Create a function called 'reverse_string' which takes a string as a parameter
# The function reverses it and returns with the reversed string

def reverse_string(str):
    rev_str = ""
    for i in range(len(str) - 1, -1, -1):
        rev_str += str[i]
    return rev_str

reversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"

print(reverse_string(reversed))