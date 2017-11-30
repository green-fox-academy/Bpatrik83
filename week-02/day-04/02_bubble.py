# Sort that list

#    Create a function that takes a list of numbers as parameter
#    Returns a list where the elements are sorted in ascending numerical order
#    Make a second boolean parameter, if it's true sort that list descending

# Example
#
#    input [34, 12, 24, 9, 5]
#    output [5, 9, 12, 24, 34]

list_input = [34, 12, 24, 9, 5]
sort_rev = False

def bubbleSort(list_input, sort_rev):
    for i in range(len(list_input)):
        for j in range(len(list_input) - 1, i, -1):
            if sort_rev:
                if list_input[j] < list_input[j - 1]:
                    tmp = list_input[j - 1]
                    list_input[j - 1] = list_input[j]
                    list_input[j] = tmp
            else:
                if list_input[j] > list_input[j - 1]:
                    tmp = list_input[j - 1]
                    list_input[j - 1] = list_input[j]
                    list_input[j] = tmp
    return list_input

print(bubbleSort(list_input, sort_rev))