def tarjan(nb, roads, num, low, stack, in_stack, visited, ans):
    stk = [[nb, 0, [[], []]]]
    while len(stk) > 0:
        nb, order = stk[-1][:2]
        if order == 0:
            num[nb] = low[nb] = len(visited)
            stack.append(nb)
            visited.add(nb)
            in_stack.add(nb)
        if order < len(roads[nb]):
            dst = roads[nb][order]
            stk[-1][1] += 1
            if dst not in visited:
                stk[-1][2][0].append(dst)
                stk.append([dst, 0, [[], []]])
            elif dst in in_stack:
                stk[-1][2][1].append(dst)
        else:
            for dst in stk[-1][2][0]:
                low[nb] = min(low[nb], low[dst])
            for dst in stk[-1][2][1]:
                low[nb] = min(low[nb], num[dst])
            if num[nb] == low[nb]:
                back = -1
                ans.append(0)
                while back != nb:
                    back = stack.pop()
                    in_stack.remove(back)
                    ans[-1] += 1
            stk.pop()


n, m = [int(it) for it in input().rstrip().split(' ')]
roads = [[] for i in range(n)]
for i in range(m):
    src, dst = [int(it) - 1 for it in input().rstrip().split(' ')]
    roads[src].append(dst)
stack = []
ans = []
num = [float('inf')] * n
low = [float('inf')] * n
in_stack = set()
visited = set()
for i in range(n):
    if i not in visited:
        tarjan(i, roads, num, low, stack, in_stack, visited, ans)
count = 0
for it in ans:
    count += it * (it - 1) // 2
print(count)
