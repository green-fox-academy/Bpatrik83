# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def change_x(str):
    if str == "":
        return ""
    if str[0] == "x":
        return "y" + change_x(str[1:])
    return str[0] + change_x(str[1:])

str = "xjhvxjhxjhxxxxxjvhxhvxxxkjkxhkxjhxxkxkxh"
print(change_x(str))

