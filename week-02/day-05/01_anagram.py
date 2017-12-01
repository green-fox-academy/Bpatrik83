# Exercise

# Create a function named is anagram following your current language's style guide.
# It should take two strings and return a boolean value depending on whether its an anagram or not.
# Examples

#   input 1 	input 2 	output
#   "dog" 	    "god" 	    true
#   "green" 	"fox" 	    false

def input_values():
    in_one = input("Enter the first word: ")
    in_two = input("Enter the second word: ")
    sorted_one = "".join(sorted(in_one.lower())).split()
    sorted_two = "".join(sorted(in_two.lower())).split()
    return sorted_one, sorted_two

def check_anagram(sorted_one, sorted_two):
    if sorted_one == sorted_two:
        return True
    return False

print(check_anagram(*input_values()))

