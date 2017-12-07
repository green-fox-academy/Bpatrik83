# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def change_x(str):
    if str == str[::-1]:
        return str[::-1]
    return str[0] + "*" + change_x(str[1:])

str = "xjhvxjhxjhxxxxxjvhxhvxxxkjkxhkxjhxxkxkxhsfdsdxsfgsfewtfioewghkljsfgbsdfgbkjs"
print(change_x(str))