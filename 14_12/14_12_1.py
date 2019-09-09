n = int(input())
a = input().rstrip().split(' ')
record = dict()
for i, it in enumerate(a):
    if it not in record:
        record[it] = 0
    record[it] += 1
    if i != n - 1:
        print(record[it], end=' ')
    else:
        print(record[it])
