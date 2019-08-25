n, l, t = eval(input().replace(' ', ','))
#balls = [int(it) for it in input().split(' ')]
balls = eval('[' + input().replace(' ', ',') + ']')

line = [[] for i in range(l + 1)]
dst = [0] * n
for i, ball in enumerate(balls):
    line[ball].append(i)
    
for i in range(t):
    old_line = line
    line = [[] for i in range(l + 1)]
    for j, it in enumerate(old_line):
        if len(it) == 1:
            if dst[it[0]] == 0:
                if j == l:
                    dst[it[0]] = 1
                    line[j - 1].append(it[0])
                else:
                    line[j + 1].append(it[0])
            else:
                if j == 0:
                    dst[it[0]] = 0
                    line[j + 1].append(it[0])
                else:
                    line[j - 1].append(it[0])
        elif len(it) == 2:
            for ball in it:
                if dst[ball] == 0:
                    line[j - 1].append(ball)
                    dst[ball] = 1
                else:
                    line[j + 1].append(ball)
                    dst[ball] = 0
                    
for j, it in enumerate(line):
    for ball in it:
        dst[ball] = j
        
print(' '.join([str(it) for it in dst]))
    
