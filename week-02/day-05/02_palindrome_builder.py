# Exercise

# Create a function named create palindrome following your current language's style guide.
# It should take a string, create a palindrome from it and then return it.
# Examples
#   input 	    output
#   "" 	        ""
#   "greenfox" 	"greenfoxxofneerg"
#   "123" 	    "123321"

def input_value():
    in_str = input("Enter a word: ")
    return in_str

def create_palindrome(in_one):
     in_one += in_one[::-1]
     return in_one

print(create_palindrome(input_value()))