n = int(input())
a = [int(it) for it in input().rstrip().split(' ')]
b = [abs(a[i] - a[i + 1]) for i in range(n - 1)]
print(max(b))
