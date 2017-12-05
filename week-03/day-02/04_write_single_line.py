# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"

def write_line(file_name):
    try:
        with open(file_name, "w") as f:
            f.writelines("Patrik_Bikes")
        return "File write done!"

    except IOError:
        return "Unable to write file: my-file.txt"

file_name = "my-file.txt"
print(write_line(file_name))
