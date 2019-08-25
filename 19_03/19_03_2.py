n = int(input())
for i in range(n):
    s = eval(input().replace('x', '*').replace('/', '//'))
    if s == 24:
        print('Yes')
    else:
        print('No')
