r, y, g = eval(input().replace(' ', ','))
n = int(input())
count = 0
for i in range(n):
    k, t = eval(input().replace(' ', ','))
    if k == 0:
        count += t
    elif k == 1:
        count += t
    elif k == 2:
        count += (t + r)
print(count)
