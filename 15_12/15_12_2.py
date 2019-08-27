import copy

n, m = [int(it) for it in input().rstrip().split()]
array = []
for i in range(n):
    array.append([int(it) for it in input().rstrip().split()])
array_cp = copy.deepcopy(array)
for i in range(n):
    for j in range(m):
        if i <= n - 3:
            if array[i][j] == array[i + 1][j] == array[i + 2][j]:
                array_cp[i][j] = array_cp[i + 1][j] = array_cp[i + 2][j] = 0
        if j <= m - 3:
            if array[i][j] == array[i][j + 1] == array[i][j + 2]:
                array_cp[i][j] = array_cp[i][j + 1] = array_cp[i][j + 2] = 0
for i in range(n):
    print(' '.join([str(it) for it in array_cp[i]]))
