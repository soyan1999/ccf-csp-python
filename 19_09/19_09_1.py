n, m = [int(it) for it in input().rstrip().split(' ')]
reg = []
cut = []
for i in range(n):
    ipts = [int(it) for it in input().rstrip().split(' ')]
    reg.append(ipts[0])
    cut.append(sum(ipts[1:]))
count = sum(reg) + sum(cut)
mini = min(cut)
idx = cut.index(mini) + 1
print('%d %d %d' % (count, idx, -mini))
