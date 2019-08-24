def dfs(src, tp, roads, st):
    for dst in roads[src][tp]:
        if dst not in st:
            st.add(dst)
            dfs(dst, tp, roads, st)


n, m = [int(it) for it in input().split(' ')]
roads = [[[], []] for it in range(n)]
for i in range(m):
    src, dst = [int(it) for it in input().strip().split(' ')]
    roads[src - 1][0].append(dst - 1)
    roads[dst - 1][1].append(src - 1)

count = 0
for i in range(n):
    st_in = {i}
    st_out = {i}
    dfs(i, 0, roads, st_in)
    dfs(i, 1, roads, st_out)
    st = st_in | st_out
    if len(st) == n:
        count += 1

print(count)
