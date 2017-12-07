# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

def ears_count(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return (ears_count(n - 1) + 3)
    else:
        return (ears_count(n - 1) + 2)

n = 21
print(ears_count(n))