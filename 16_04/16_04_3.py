import re


def nmlz_path(path):
    path = re.sub(r'[/]+', r'/', path)
    if len(path) > 1 and path[-1] == '/':
        path = path[:-1]
    return path


p = int(input())
cd = nmlz_path(input().rstrip())
for i in range(p):
    path = nmlz_path(input().rstrip())
    if path == '':
        path = cd
    elif path[0] == '/':
        path = path
    else:
        path = cd + '/' + path
    path = path[1:]
    names = path.split('/')
    stack = []
    for name in names:
        if name == '..':
            if len(stack) != 0:
                stack.pop()
        elif name == '.':
            pass
        else:
            stack.append(name)
    print('/' + '/'.join(stack))
