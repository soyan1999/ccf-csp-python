import re

n, m = input().split(' ')
n = int(n)
m = int(m)

pat = re.compile(r'<int>|<str>|<path>')

pts = []
for i in range(n):
    pt, name = input().split(' ')

    int_mark = []
    for j, pa in enumerate(pat.findall(pt)):
        if pa == '<int>':
            int_mark.append(j)

    pt = pt.replace('<int>', '([0-9]+)')
    pt = pt.replace('<str>', '([^/]+)')
    pt = pt.replace('<path>', '(.+)')
    pt = '^' + pt + '$'
    pts.append((re.compile(pt), name, int_mark))

for i in range(m):
    matched = False
    url = input()
    for pt, name, int_mark in pts:
        res = pt.match(url)
        if res != None:
            res = list(res.groups())
            for j in int_mark:
                res[j] = str(int(res[j]))
            print(' '.join([name] + res))
            matched = True
            break
    if matched == False:
        print('404')
