n, m = [int(it) for it in input().rstrip().split(' ')]
graph = [[] for i in range(n)]
one_nd = set()
for i in range(m):
    src, dst = [int(it) for it in input().rstrip().split(' ')]
    graph[src - 1].append(dst - 1)
    graph[dst - 1].append(src - 1)
for i in range(n):
    graph[i].sort(reverse=True)
    if len(graph[i]) % 2 == 1:
        one_nd.add(i)
if 0 in one_nd and len(one_nd) != 2:
    print(-1)
elif 0 not in one_nd and len(one_nd) != 0:
    print(-1)
else:
    path = [0]
    circuit = []
    while len(path) != 0 and len(path) + len(circuit) <= m:
        now = path[-1]
        if len(graph[now]) == 0:
            circuit.append(path.pop())
        else:
            nxt = graph[now].pop()
            graph[nxt].remove(now)
            path.append(nxt)
    if len(path) == 0:
        print(-1)
    else:
        circuit.reverse()
        path.extend(circuit)
        print(' '.join(str(it + 1) for it in path))
