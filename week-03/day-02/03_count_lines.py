# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

def count_lines(file_name):
    try:
        with open(file_name) as f:
            count = 1
            for i in enumerate(f):
                count += 1
            return count
    except IOError:
        return 0

file_name = "my-file.txt"
print(count_lines(file_name))
