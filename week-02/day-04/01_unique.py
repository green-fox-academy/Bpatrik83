# Unique - remove the duplicates

#    Create a function that takes a list of numbers as a parameter
#    Returns a list of numbers where every number in the list occurs only once

# Example

#    input: [1, 11, 34, 11, 52, 61, 1, 34]
#    output: [1, 11, 34, 52, 61]

list_original = [1, 11, 34, 11, 52, 61, 1, 34]

def check(list_original):
    list_output = []
    for i in list_original:
          if i not in list_output:
             list_output.append(i)
    return list_output

print(check(list_original))
