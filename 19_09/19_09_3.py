def out(ss):
    for s in ss:
        print(r'\x'+'%02X' % (ord(s),), end='')


def slt(clr, is_emp, bef):
    if is_emp:
        if clr == bef:
            out(' ')
        elif clr != (0, 0, 0):
            out('\x1b[48;2;%d;%d;%dm ' % (clr[0], clr[1], clr[2]))
        else:
            out('\x1b[0m ')
    else:
        if bef != (0, 0, 0):
            out('\x1b[0m\n')
        else:
            out('\n')


m, n = [int(it) for it in input().rstrip().split(' ')]
p, q = [int(it) for it in input().rstrip().split(' ')]
x_num = m // p
y_num = n // q
div = p * q
graph_ = []
for i in range(n):
    graph_.append([])
    for j in range(m):
        ipt = input()[1:]
        if len(ipt) == 1:
            clr = ipt * 6
        elif len(ipt) == 3:
            clr = ipt[0] * 2 + ipt[1] * 2 + ipt[2] * 2
        else:
            clr = ipt
        r = int('0x' + clr[0:2], 16)
        g = int('0x' + clr[2:4], 16)
        b = int('0x' + clr[4:6], 16)
        graph_[-1].append((r, g, b))
graph = []
for i in range(y_num):
    graph.append([])
    for j in range(x_num):
        r = g = b = 0
        for y in range(i * q, i * q + q):
            for x in range(j * p, j * p + p):
                r += graph_[y][x][0]
                g += graph_[y][x][1]
                b += graph_[y][x][2]
        r //= div
        g //= div
        b //= div
        graph[-1].append((r, g, b))
bef = (0, 0, 0)
reg = (0, 0, 0)
for i in range(y_num):
    for j in range(x_num):
        slt(graph[i][j], True, bef)
        bef = graph[i][j]
    slt(reg, False, bef)
    bef = reg
