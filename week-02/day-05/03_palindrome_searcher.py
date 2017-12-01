# Exercise
# Create a function named search palindrome following your current language's style guide.
# It should take a string, search for palindromes that at least 3 characters long and return a list with the found palindromes.
# Examples
#           input 	                            output
#           "dog goat dad duck doodle never" 	["og go", "g g", " dad ", "dad", "d d", "dood", "eve"]
#           "apple" 	                        []
#           "racecar" 	                        ["racecar", "aceca", "cec"]
#           "" 	                                []




def search_palindromes(input_text):
    list_palindromes = []
    for i in range(1, len(input_text) - 1):
        if input_text[i - 2:i] == (input_text[i:i + 2])[::-1]:
            j = 2
            while input_text[i - j:i] == input_text[i:i + j][::-1]:
                list_palindromes.append((input_text[i - j:i + j]))
                j += 1
                if i + j == len(input_text):
                    return list_palindromes
        if input_text[i - 1] == input_text[i + 1]:
            j = 1
            while input_text[i - j] == input_text[i + j]:
                list_palindromes.append((input_text[i - j:i + j + 1]))
                j += 1
                if i + j == len(input_text):
                    return list_palindromes
    return list_palindromes

list_test =["dog goat dad duck doodle never", "apple", "racecar", "", "trart geekkeeg apple"]
for i in list_test:
    print(search_palindromes(i))

