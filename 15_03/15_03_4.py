import sys
sys.setrecursionlimit(100000)


def get_best(length):
    length_cp = length[:]
    longest = max(length)
    if len(length) > 1:
        length_cp.remove(longest)
        sec = max(length_cp)
        return (longest, longest + sec)
    else:
        return (longest, longest)


def dfs(num, tree, ans):
    if len(tree[num]) == 0:
        return (0, 0)
    best = 0
    for child in tree[num]:
        longest, best_ = dfs(child, tree, ans)
        best = max(best, best_)
        ans[num].append(longest + 1)
    longest, best_ = get_best(ans[num])
    best = max(best, best_)
    return (longest, best)


n, m = [int(it) for it in input().rstrip().split(' ')]
ns = [int(it) - 1 for it in input().rstrip().split(' ')]
ms = [int(it) - 1 for it in input().rstrip().split(' ')]
tree = [[] for i in range(n + m)]
ans = [[] for i in range(n + m)]
for child, root in enumerate(ns):
    tree[root].append(child + 1)
for child, root in enumerate(ms):
    tree[root].append(child + n)
longest, best = dfs(0, tree, ans)
print(best)
