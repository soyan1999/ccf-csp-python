def slt(begin, end, weights, anws):
    if anws[begin][end] != -1:
        return anws[begin][end]
    if begin == end:
        anws[begin][end] = 0
        return 0
    mini = float('inf')
    for i in range(begin, end):
        anw_l = slt(begin, i, weights, anws)
        anw_r = slt(i + 1, end, weights, anws)
        mini = min(mini, anw_l + anw_r)
    anws[begin][end] = mini + weights[begin][end]
    return anws[begin][end]


n = int(input())
a = [int(it) for it in input().rstrip().split(' ')]
weights = [[0] * n for i in range(n)]
anws = [[-1] * n for i in range(n)]
for i in range(n):
    for j in range(i, n):
        if j == i:
            weights[i][j] = a[i]
        else:
            weights[i][j] = weights[i][j - 1] + a[j]
print(slt(0, n - 1, weights, anws))
