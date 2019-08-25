n = int(input())
a = [int(it) for it in input().rstrip().split(' ')]
a.sort()
mid = a[n // 2]
l_count = 0
r_count = 0
for it in a:
    if it > mid:
        r_count += 1
    elif it < mid:
        l_count += 1

print(mid if l_count == r_count else - 1)
