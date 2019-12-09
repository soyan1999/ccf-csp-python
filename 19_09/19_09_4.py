from heapq import heapify, heappop, heappush
import re

m, n = [int(it) for it in input().rstrip().split(' ')]
ban = set()
inf = dict()
goods = []
for i in range(n):
    ids, score = [int(it) for it in input().rstrip().split(' ')]
    for j in range(m):
        goods.append((-score, j, ids))
        inf[(j, ids)] = -score
op_num = int(input())
heapify(goods)
for i in range(op_num):
    ipts = [int(it) for it in re.split(' +', input().rstrip())]
    if ipts[0] == 1:
        heappush(goods, (-ipts[3], ipts[1], ipts[2]))
        inf[(ipts[1], ipts[2])] = -ipts[3]
        if (-ipts[3], ipts[1], ipts[2]) in ban:
            ban.remove((-ipts[3], ipts[1], ipts[2]))
    elif ipts[0] == 2:
        score = inf[(ipts[1], ipts[2])]
        ban.add((score, ipts[1], ipts[2]))
    else:
        goods_ = goods.copy()
        k_ = ipts[1]
        ks = ipts[2:]
        k_ = min(k_, sum(ks))
        slts = [[] for j in range(m)]
        while len(goods_) > 0 and k_ > 0:
            score, tp, ids = heappop(goods_)
            if (score, tp, ids) not in ban and ks[tp] > 0:
                slts[tp].append(ids)
                ks[tp] -= 1
                k_ -= 1
        for j in range(m):
            if len(slts[j]) == 0:
                print(-1)
            else:
                print(' '.join([str(it) for it in slts[j]]))
