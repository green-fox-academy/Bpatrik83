# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def delete_x(str):
    if str == "":
        return ""
    if str[0] == "x":
        return "" + delete_x(str[1:])
    return str[0] + delete_x(str[1:])

str = "xjhvxjhxjhxxxxxjvhxhvxxxkjkxhkxjhxxkxkxh"
print(delete_x(str))