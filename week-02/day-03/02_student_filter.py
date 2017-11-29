students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints:
#  - how many candies they have on average

def moreCandy():
    for i in students:
        if i.get('candies') > 4:
            print(i.get('name'))

def sumAge():
    sum = 0
    count = 0
    for i in students:
        sum += i.get('candies')
        count += 1
    print(sum / count)



moreCandy()
sumAge()