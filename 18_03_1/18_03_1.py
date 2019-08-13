steps = input().split(' ')
count = 0
last = 0
for it in steps:
    if it == '0':
        print(count)
        break
    elif it == '1':
        count += 1
        last = 1
    else:
        if last < 2:
            count += 2
            last = 2
        else:
            count += last + 2
            last += 2
