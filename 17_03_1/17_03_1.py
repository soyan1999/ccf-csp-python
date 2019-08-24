n, k = [int(it) for it in input().strip().split(' ')]
a = [int(it) for it in input().strip().split(' ')]
a.reverse()
count = 0
w = 0
while count < n and len(a) > 0:
    w_ = a.pop()
    w += w_
    if w >= k or len(a) == 0:
        count += 1
        w = 0

print(count)
