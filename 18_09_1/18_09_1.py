n = int(input())
first_price = eval('['+input().replace(' ', ',')+']')
second_price = []
for i in range(n):
    if i == 0:
        price = (first_price[0] + first_price[1]) // 2
    elif i == n - 1:
        price = (first_price[-1] + first_price[-2]) // 2
    else:
        price = (first_price[i - 1] + first_price[i] + first_price[i + 1]) // 3
    second_price.append(str(price))
print(' '.join(second_price))
