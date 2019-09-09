from datetime import date, timedelta


a, b, c, y1, y2 = [int(it) for it in input().rstrip().split(' ')]
if y2 < y1:
    y1, y2 = y2, y1
for year in range(y1, y2 + 1):
    now = date(year, a, 1)
    week = now.weekday()
    day = (b - 1) * 7 + c - week
    day = day + 7 if c <= week else day
    now = now + timedelta(days=day - 1)
    if now.month != a:
        print('none')
    else:
        print('%d/%02d/%02d' % (year, now.month, now.day))
