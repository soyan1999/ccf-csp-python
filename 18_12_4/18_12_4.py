from heapq import heapify, heappop, heappush
from collections import defaultdict


n = int(input())
m = int(input())
root = int(input()) - 1
road_set = defaultdict(list)
max_length = -1

for i in range(m):
    src, dst, length = [int(item) for item in input().split(' ')]
    road_set[src - 1].append((length, dst - 1))
    road_set[dst - 1].append((length, src - 1))

in_set = {root}
heap = [(item + (item[0],)) for item in road_set[root]]
heapify(heap)

while len(in_set) < n and len(heap) != 0:
    dis, dst, length = heappop(heap)
    if dst not in in_set:
        in_set.add(dst)
        if length > max_length:
            max_length = length
        for ln, dt in road_set[dst]:
            if dt not in in_set:
                heappush(heap, (dst + ln, dt, ln))

print(max_length)

