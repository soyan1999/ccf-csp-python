n, m = [int(it) for it in input().rstrip().split(' ')]
graph = []
for i in range(n):
    row = input().rstrip().split(' ')
    row.reverse()
    graph.append(row)
for j in range(m):
    print(' '.join([graph[i][j] for i in range(n)]))
