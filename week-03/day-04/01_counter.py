# Write a recursive function that takes one parameter: n and counts down from n.

def calc_factorial(n):
    if n == 0:
        return 0
    else:
        print(n)
        return (calc_factorial(n - 1))

num = 50
calc_factorial(num)