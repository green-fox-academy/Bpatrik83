# Find part of an integer

#    Create a function that takes two strings as a parameter
#    Returns the starting index where the second one is starting in the first one
#    Returns -1 if the second string is not in the first one

# Example

#    input: "this is what I'm searching in", "searching"
#    output: 17

text = "this is what I'm searching in"
str = "searching"

def finder(text, str):
    for i in range(0, len(text)- len(str), 1):
        if str == text[i:i+len(str)]:
            return i
    return -1

print(finder(text, str))