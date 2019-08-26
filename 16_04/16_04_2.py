place = []
diamond = []
for i in range(15):
    place.append([int(it) for it in input().rstrip().split(' ')])
for i in range(4):
    diamond.append([int(it) for it in input().rstrip().split(' ')])
mv_x = int(input()) - 1
edg_down = []
edg_up = []
for i in range(10):
    edg = 15
    for j in range(15):
        if place[14 - j][i] == 1:
            edg = 14 - j
    edg_down.append(edg)
for i in range(4):
    edg = -100
    for j in range(4):
        if diamond[j][i] == 1:
            edg = j + 1
    edg_up.append(edg)

mv_y = min([(down - up) for down, up in zip(edg_down[mv_x:mv_x + 4], edg_up)])
for i in range(mv_x, mv_x + 4):
    for j in range(mv_y, mv_y + 4):
        if diamond[j - mv_y][i - mv_x] == 1:
            place[j][i] = 1
for i in range(15):
    print(' '.join([str(it) for it in place[i]]))
