n = int(input())
day2 = [int(it) for it in input().split(' ')]

day1 = [0] * n
ban = [set() for i in range(n)]
slt = [[] for i in range(n)]
slt[0] = [(day2[0] * 2 - i) for i in range(day2[0] * 2)]

i = 0
while i < n:
    if len(slt[i]) > 0:
        day1[i] = slt[i].pop()
    else:
        if i > 1:
            ban[i - 1].add((day1[i - 2], day1[i - 1]))
        i -= 1
        continue
    if i > 0:
        if (day1[i - 1], day1[i]) in ban[i]:
            continue
    if i == 0:
        slt[1] = []
        prc = day2[0] * 2 - day1[0]
        if prc + 1> 0:
            slt[1].append(prc + 1)
        if prc > 0:
            slt[1].append(prc)
        i += 1
    elif i == n - 1:
        if (day1[i - 1] + day1[i]) // 2 == day2[i]:
            i += 1
    else:
        slt[i + 1] = []
        prc = day2[i] * 3 - day1[i - 1] - day1[i]
        if prc + 2> 0:
            slt[i + 1].append(prc + 2)
        if prc + 1 > 0:
            slt[i + 1].append(prc + 1)
        if prc > 0:
            slt[i + 1].append(prc)
        i += 1
        
print(' '.join([str(it) for it in day1]))
