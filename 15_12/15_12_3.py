def line(x1, y1, x2, y2, graph):
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            if graph[i][x1] not in {'-', '+'}:
                graph[i][x1] = '|'
            else:
                graph[i][x1] = '+'
    else:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            if graph[y1][i] not in {'|', '+'}:
                graph[y1][i] = '-'
            else:
                graph[y1][i] = '+'


def fill(x, y, c, graph):
    done_set = set()
    stack = [(x, y)]
    ban_set = {'|', '-', '+'}
    while len(stack) > 0:
        x, y = stack.pop()
        if (x, y) not in done_set:
            graph[y][x] = c
            done_set.add((x, y))
            if x < len(graph[0]) - 1 and graph[y][x + 1] not in ban_set and (x + 1, y) not in done_set:
                stack.append((x + 1, y))
            if x > 0 and graph[y][x - 1] not in ban_set and (x - 1, y) not in done_set:
                stack.append((x - 1, y))
            if y < len(graph) - 1 and graph[y + 1][x] not in ban_set and (x, y + 1) not in done_set:
                stack.append((x, y + 1))
            if y > 0 and graph[y - 1][x] not in ban_set and (x, y - 1) not in done_set:
                stack.append((x, y - 1))


m, n, q = [int(it) for it in input().rstrip().split(' ')]
graph = [['.'] * m for i in range(n)]
for i in range(q):
    ips = input().rstrip().split(' ')
    if len(ips) == 5:
        line(int(ips[1]), int(ips[2]), int(ips[3]), int(ips[4]), graph)
    else:
        fill(int(ips[1]), int(ips[2]), ips[3], graph)
graph.reverse()
for i in range(n):
    print(''.join(graph[i]))
