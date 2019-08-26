n = int(input())
a = [int(it) for it in input().rstrip().split(' ')]
count = 0
for i in range(1, n - 1):
    if (a[i - 1] - a[i]) * (a[i + 1] - a[i]) > 0:
        count += 1
print(count)
