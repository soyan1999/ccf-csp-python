def slt(r, c, count, inf, ban_set):
    if inf[0] + inf[1] - r - c + count >= inf[2]:
        return
    if r == inf[0] and c == inf[1]:
        inf[2] = count
        return
    if (r, c, count) in ban_set:
        return
    if r < inf[0]:
        slt(r + 1, c, count + 1, inf, ban_set)
    if c < inf[1]:
        slt(r, c + 1, count + 1, inf, ban_set)
    if r > 1:
        slt(r - 1, c, count + 1, inf, ban_set)
    if c > 1:
        slt(r, c - 1, count + 1, inf, ban_set)
    ban_set.add((r, c, count))
    return


n, m, t = [int(it) for it in input().rstrip().split(' ')]
ban_set = set()
inf = [n, m, float('inf')]
for i in range(t):
    r, c, a, b = [int(it) for it in input().rstrip().split(' ')]
    for j in range(a, b + 1):
        ban_set.add((r, c, j))
slt(1, 1, 0, inf, ban_set)
print(inf[2])
