n = int(input())
cube = [[False] * 100 for i in range(100)]
for k in range(n):
    x1, y1, x2, y2 = [int(it) for it in input().rstrip().split(' ')]
    for i in range(y1, y2):
        for j in range(x1, x2):
            cube[i][j] = True
count = 0
for i in range(100):
    for j in range(100):
        if cube[i][j] == True:
            count += 1
print(count)
