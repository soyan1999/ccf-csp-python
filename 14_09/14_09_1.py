n = int(input())
a = [int(it) for it in input().rstrip().split(' ')]
a.sort()
count = 0
for i in range(n - 1):
    if abs(a[i] - a[i + 1]) == 1:
        count += 1
print(count)
