# - Write a function called `sum` that sum all the numbers
#   until the given parameter

def sum(numList):
    theSum = 0
    for i in range(len(numList)):
        theSum += numList[i]
    return theSum

print(sum([1, 3, 5, 7, 9]))

