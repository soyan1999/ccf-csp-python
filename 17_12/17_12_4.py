from collections import defaultdict
from heapq import heapify, heappop, heappush


n, m = eval(input().replace(' ', ','))
road_set = defaultdict(list)
length_set = defaultdict(list)

for i in range(m):
    t, a, b, c = [int(it) for it in input().split(' ')]
    road_set[a - 1].append((c, t, b - 1))
    road_set[b - 1].append((c, t, a - 1))

heap = []
for c, t, d in road_set[0]:
    if t == 0:
        heap.append((c, 0, d))
    else:
        heap.append((c * c, c, d))
length_set[0] = [(0, 0)]
heapify(heap)

while n - 1 not in length_set:
    dis, tp, dst = heappop(heap)
    if dst not in length_set or length_set[dst][-1][1] > tp:
        length_set[dst].append((dis, tp))
        for c, t, nxt in road_set[dst]:
            dis_ = dis + c if t == 0 else dis - tp * tp + (tp + c) * (tp + c)
            tp_ = 0 if t == 0 else tp + c
            if nxt not in length_set or length_set[nxt][-1][1] > tp_:
                heappush(heap, (dis_, tp_, nxt))

print(length_set[n - 1][0][0])
