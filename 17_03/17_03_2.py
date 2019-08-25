n = int(input())
m = int(input())
queue = [(it + 1) for it in range(n)]
for i in range(m):
    num, mv = [int(it) for it in input().strip().split(' ')]
    index = queue.index(num)
    del queue[index]
    queue.insert(index + mv, num)

print(' '.join([str(it) for it in queue]))
