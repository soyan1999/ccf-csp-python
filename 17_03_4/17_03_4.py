from heapq import heapify, heappop, heappush
from collections import defaultdict


n, m = [int(item) for item in input().rstrip().split(' ')]
road_set = defaultdict(list)
max_length = -1

for i in range(m):
    src, dst, length = [int(item) for item in input().rstrip().split(' ')]
    road_set[src - 1].append((length, dst - 1))
    road_set[dst - 1].append((length, src - 1))

in_set = {0}
heap = road_set[0][:]
heapify(heap)

while (n-1) not in in_set and len(heap) != 0:
    length, dst = heappop(heap)
    if dst not in in_set:
        in_set.add(dst)
        max_length = max(length, max_length)
        for ln, dt in road_set[dst]:
            if dt not in in_set:
                heappush(heap, (ln, dt))

print(max_length)
