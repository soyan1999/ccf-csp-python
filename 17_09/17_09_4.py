def tarjan(nb, graph, num, low, stack, in_stack, visited, ans, ans_):
    num[nb] = low[nb] = len(visited)
    stack.append(nb)
    visited.add(nb)
    in_stack.add(nb)
    for dst in graph[nb][0]:
        if dst not in visited:
            tarjan(dst, graph, num, low, stack, in_stack, visited, ans, ans_)
            low[nb] = min(low[nb], low[dst])
        elif dst in in_stack:
            low[nb] = min(low[nb], num[dst])
    if num[nb] == low[nb]:
        out = -1
        ans.append(set())
        while out != nb:
            out = stack.pop()
            in_stack.remove(out)
            ans[-1].add(out)
            ans_[out] = len(ans) - 1


def dfs(nb, tree, tree_child, ans, visited):
    visited.add(nb)
    for dst in tree[nb]:
        if dst not in visited:
            dfs(dst, tree, tree_child, ans, visited)
        tree_child[nb] |= ans[dst] | tree_child[dst]


n, m = [int(it) for it in input().rstrip().split(' ')]
graph = [[[], []] for i in range(n)]
for i in range(m):
    src, dst = [int(it) - 1 for it in input().rstrip().split(' ')]
    graph[src][0].append(dst)
    graph[dst][1].append(src)
stack = []
ans = []
ans_ = [-1] * n
num = [-1] * n
low = [-1] * n
in_stack = set()
visited = set()
for i in range(n):
    if i not in visited:
        tarjan(i, graph, num, low, stack, in_stack, visited, ans, ans_)
tree = []
tree_ = []
tree_child = [set() for i in range(len(ans))]
tree_child_ = [set() for i in range(len(ans))]
visited = set()
visited_ = set()
for i, an in enumerate(ans):
    tree.append(set())
    tree_.append(set())
    for a in an:
        for dst in graph[a][0]:
            tree[-1].add(ans_[dst])
        for src in graph[a][1]:
            tree_[-1].add(ans_[src])
    if i in tree[-1]:
        tree[-1].remove(i)
    if i in tree_[-1]:
        tree_[-1].remove(i)

for i in range(len(ans)):
    if i not in visited:
        dfs(i, tree, tree_child, ans, visited)
    if i not in visited_:
        dfs(i, tree_, tree_child_, ans, visited_)
count = 0
for i in range(len(ans)):
    if len(tree_child[i]) + len(tree_child_[i]) + len(ans[i]) == n:
        count += len(ans[i])
print(count)
