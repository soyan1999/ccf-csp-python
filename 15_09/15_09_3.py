import re
from collections import defaultdict

m, n = [int(it) for it in input().rstrip().split(' ')]
lines = []
mode = defaultdict(str)
for i in range(m):
    lines.append(input())
for i in range(n):
    name, value = input()[:-1].split(' "')
    mode[name] = value
for i in range(m):
    for it in re.findall(r'\{\{ .+? \}\}', lines[i]):
        lines[i] = lines[i].replace(it, mode[it[3:-3]])
    print(lines[i])
