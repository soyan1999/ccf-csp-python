n = int(input())
a = [int(it) for it in input().rstrip().split(' ')]
ans = []
visited = set()
for it in a:
    if it not in visited:
        ans.append((-a.count(it), it))
        visited.add(it)
ans.sort()
for count, it in ans:
    print('%d %d' % (it, -count))
