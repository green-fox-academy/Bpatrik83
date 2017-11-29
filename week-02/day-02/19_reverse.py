# - Create a variable named `aj`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements in `aj`
# - Print the elements of the reversed `aj`

aj = [3, 4, 5, 6, 7]

aj.reverse()
print(aj)
aj.reverse()

rev_aj = []

for i in range(len(aj) - 1, -1, -1):
     rev_aj.append(aj[i])

print(rev_aj)