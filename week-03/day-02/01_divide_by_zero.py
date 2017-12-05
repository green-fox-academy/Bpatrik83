# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

def divide_ten(number):
    try:
        return 10 / number
    except ZeroDivisionError:
        return "fail"

print(divide_ten(0))
