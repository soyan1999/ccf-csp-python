import sys


def cancel(num, lines):
    if lines[num][:6] != 'cancel':
        lines[num][1] = not lines[num][1]
    else:
        cancel(int(lines[num][7:]) - 1, lines)


lines = [[line.rstrip(), True] for line in sys.stdin]
for line, _ in lines:
    if line[:6] == 'cancel':
        cancel(int(line[7:]) - 1, lines)
buys = []
sells = []
prices = set()
buy_count = sell_count = 0
for line, enable in lines:
    if enable:
        li = line.split(' ')
        if li[0] == 'buy':
            buys.append((float(li[1]), int(li[2])))
            buy_count += int(li[2])
            prices.add(float(li[1]))
        elif li[0] == 'sell':
            sells.append((float(li[1]), int(li[2])))
            prices.add(float(li[1]))
buys.sort()
sells.sort()
prices = list(prices)
prices.sort()
buy_idx = sell_idx = 0
best = 0
best_price = 0
for price in prices:
    while buy_idx < len(buys) and buys[buy_idx][0] < price:
        buy_count -= buys[buy_idx][1]
        buy_idx += 1
    while sell_idx < len(sells) and sells[sell_idx][0] <= price:
        sell_count += sells[sell_idx][1]
        sell_idx += 1
    num = min(buy_count, sell_count)
    if num >= best:
        best = num
        best_price = price
print('%.2f %d' % (best_price, best))
