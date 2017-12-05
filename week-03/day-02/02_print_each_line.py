# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"

def read_lines(file_name):
    try:
        with open(file_name) as f:
            return f.read()
    except IOError:
        return "Unable to read file: ", file_name

file_name = "my-file.txt"
print(read_lines(file_name))