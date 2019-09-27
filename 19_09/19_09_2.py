n = int(input())
reg = []
if_drop = [False] * n
for i in range(n):
    ipts = [int(it) for it in input().rstrip().split(' ')]
    bef = ipts[1]
    for j in range(2, ipts[0] + 1):
        if ipts[j] > 0:
            if bef != ipts[j]:
                if_drop[i] = True
                bef = ipts[j]
        else:
            bef += ipts[j]
    reg.append(bef)
count = sum(reg)
drop_num = if_drop.count(True)
e = 0
if n > 2:
    for i in range(n):
        if if_drop[i - 2] == if_drop[i - 1] == if_drop[i] == True:
            e += 1
print('%d %d %d' % (count, drop_num, e))
