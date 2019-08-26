from heapq import heapify, heappop, heappush
from collections import defaultdict


n, m = [int(item) for item in input().rstrip().split(' ')]
road_set = defaultdict(list)
all_length = 0

for i in range(m):
    src, dst, length = [int(item) for item in input().rstrip().split(' ')]
    road_set[src - 1].append((length, dst - 1))
    road_set[dst - 1].append((length, src - 1))

in_set = {0}
heap = [(item + (item[0],)) for item in road_set[0]]
heapify(heap)

while len(in_set) < n and len(heap) != 0:
    dis, dst, length = heappop(heap)
    if dst not in in_set:
        in_set.add(dst)
        all_length += length
        for ln, dt in road_set[dst]:
            if dt not in in_set:
                heappush(heap, (dis + ln, dt, ln))

print(all_length)
