n, m = input().split(' ')
n = int(n)
m = int(m)

tree = []
for i in range(n):
    item = input()
    deepth = item.count('.') // 2
    if ' ' in item:
        tag, id = item.split(' ')
        tag = tag[deepth * 2:].lower()
        tree.append((deepth, tag, id))
    else:
        tag = item[deepth * 2:].lower()
        tree.append((deepth, tag, '#'))

for i in range(m):
    search = input().split(' ')
    for j in range(len(search)):
        if search[j][0] != '#':
            search[j] = search[j].lower()
    record = []
    selected = []
    for j in range(n):
        while True:
            if len(record) == 0:
                break
            if record[-1] >= tree[j][0]:
                record.pop()
            else:
                break
        if search[len(record)] == tree[j][1] or search[len(record)] == tree[j][2]:
            if len(record) == len(search) - 1:
                selected.append(j + 1)
            else:
                record.append(tree[j][0])
    if len(selected) == 0:
        print('0')
    else:
        print('%d %s' % (len(selected), ' '.join(
            [str(it) for it in selected])))
