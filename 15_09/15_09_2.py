from datetime import datetime, timedelta

year = int(input())
day = int(input())
now = datetime(year, 1, 1) + timedelta(days=day - 1)
print(now.month)
print(now.day)
