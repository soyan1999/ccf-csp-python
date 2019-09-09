n = int(input())
cube = []
for i in range(n):
    cube.append([it for it in input().rstrip().split(' ')])
i = j = 0
state = 0
while True:
    if i == n - 1 and j == n - 1:
        print(cube[i][j])
        break
    print(cube[i][j], end=' ')
    if state == 0:
        j += 1
        if i == 0:
            state = 1
        else:
            state = 2
    elif state == 1:
        i += 1
        j -= 1
        if i == n - 1:
            state = 0
        elif j == 0:
            state = 3
    elif state == 2:
        i -= 1
        j += 1
        if j == n - 1:
            state = 3
        elif i == 0:
            state = 0
    else:
        i += 1
        if j == 0:
            state = 2
        else:
            state = 1
