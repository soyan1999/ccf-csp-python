n = int(input())
h_time = set()
w_time = set()
count = 0
for i in range(n):
    begin, end = input().split(' ')
    begin = int(begin)
    end = int(end)
    for j in range(begin, end):
        h_time.add(j)
for i in range(n):
    begin, end = input().split(' ')
    begin = int(begin)
    end = int(end)
    for j in range(begin, end):
        w_time.add(j)

print(len(h_time & w_time))
        