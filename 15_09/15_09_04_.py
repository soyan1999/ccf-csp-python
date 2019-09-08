import sys
sys.setrecursionlimit(100000)


class slt:
    def __init__(self, roads):
        self.roads = roads
        self.num = [float('inf')]*len(self.roads)
        self.low = [float('inf')]*len(self.roads)
        self.stack = []
        self.ans = []
        self.in_stack = set()
        self.visited = set()

    def tarjan(self, nb):
        self.num[nb] = self.low[nb] = len(self.visited)
        self.stack.append(nb)
        self.visited.add(nb)
        self.in_stack.add(nb)
        for dst in self.roads[nb]:
            if dst not in self.visited:
                self.tarjan(dst)
                self.low[nb] = min(self.low[nb], self.low[dst])
            elif dst in self.in_stack:
                self.low[nb] = min(self.low[nb], self.num[dst])
        if self.low[nb] == self.num[nb]:
            back = -1
            self.ans.append(0)
            while back != nb:
                back = self.stack.pop()
                self.in_stack.remove(back)
                self.ans[-1] += 1

    def out(self):
        for i in range(len(self.roads)):
            if i not in self.visited:
                self.tarjan(i)
        count = 0
        for it in self.ans:
            count += it * (it - 1) // 2
        print(count)


n, m = [int(it) for it in input().rstrip().split(' ')]
roads = [[] for i in range(n)]
for i in range(m):
    src, dst = [int(it) - 1 for it in input().rstrip().split(' ')]
    roads[src].append(dst)
ss = slt(roads)
ss.out()
