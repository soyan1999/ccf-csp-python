r, y, g = [int(item) for item in input().split(' ')]
n = int(input())
count = 0
for i in range(n):
    k, t = [int(item) for item in input().split(' ')]

    if k == 0:
        count += t
    else:
        if k == 1:
            begin_time = r - t
        elif k == 2:
            begin_time = r + y + g - t
        else:
            begin_time = r + g - t
        now_time = (begin_time + count) % (r + y + g)
        if now_time < r:
            count += r - now_time
        elif now_time < r + g:
            pass
        else:
            count += r + (r + y + g - now_time)
print(count)
