# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases

def unique_characters(test):
    dict_of_all_chars = {}
    list_of_unique_chars = []

    for char in test:
        if char not in dict_of_all_chars:
            dict_of_all_chars[char] = 1
        else:
            dict_of_all_chars[char] += 1

    for items in dict_of_all_chars:
        if dict_of_all_chars[items] == 1:
            list_of_unique_chars.append(items)

    return list_of_unique_chars



print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]