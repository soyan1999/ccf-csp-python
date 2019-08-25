n, k = eval(input().replace(' ', ','))
count = 0
out = set()
while True:
    for i in range(n):
        if i not in out:
            if len(out) == n - 1:
                print(i + 1)
                exit(0)
            count += 1
            if count % k == 0 or count % 10 == k:
                out.add(i)
