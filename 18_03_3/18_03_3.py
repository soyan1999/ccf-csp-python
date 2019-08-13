import re

n, m = input().split(' ')
n = int(n), m = int(m)

pts = []
for i in range(n):
    pt, name = input().split(' ')
    pt = pt.replace('<int>', '([0-9]+)')
    pt = pt.replace('<str>', '([^/]+)')
    pt = pt.replace('<path>', '(.+)')
    pt = '^' +pt + '$'
    pts.append((re.compile(pt), name))
    
for i in range(m):
    matched = False
    url = input()
    for pt, name in pts:
        res = pt.match(url)
        if res != None:
            print(name + ' '.join(res.groups()))
            matched = True
            break
    if matched == False:
        print('404')
