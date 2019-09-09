n = int(input())
a = [int(it) for it in input().rstrip().split(' ')]
bef = -1
count = 0
for it in a:
    if it != bef:
        count += 1
    bef = it
print(count)
