# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def compute_recur(n):
    base = 2
    if n == 1:
        return 1
    else:
        return (base * compute_recur(n - 1))

n = 10
print(compute_recur(n + 1))