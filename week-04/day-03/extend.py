# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Returns the median value of a list given as param
def median(pool):
    numbers_sum = 0
    for item in pool:
        numbers_sum += item
    return numbers_sum / len(pool)

# Returns true if the param is a vovel
def is_vovel(char):
    if char.lower() in 'aeiouéáőűöüóíú':
        return True
    return False

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = ""
    for index in range(len(hungarian)):
        if is_vovel(hungarian[index]):
            teve += hungarian[index] + "v" + hungarian[index]
        else:
            teve += hungarian[index]

    return teve