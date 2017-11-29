# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output


n = 4
list_2d = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            list_2d[i][j] = 1
        print(list_2d[i][j], end=' ')
    print()
