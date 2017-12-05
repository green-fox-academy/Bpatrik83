# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copy_file(file_01, file_02):
    try:
        with open(file_01, "r") as f:
            lines = f.read()
        with open(file_02, "w") as f1:
            f1.writelines(lines)
        return "File copy done!"
    except IOError:
        return "Unable to open file:", file_01

file_01 = "multiple-file.txt"
file_02 = "my-file.txt"
print(copy_file(file_01, file_02))