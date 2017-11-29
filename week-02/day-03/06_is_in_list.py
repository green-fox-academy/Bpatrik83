# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

def checker(contain):
    contain = False
    for i in range(len(list_of_check)):
        if list_of_check[i] in list_of_numbers:
            contain = True
        else:
            contain = False
            break
    return contain

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
list_of_check = [4, 8 ,12, 16]

print(checker(list_of_check))