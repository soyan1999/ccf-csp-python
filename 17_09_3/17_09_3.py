import json


def find(j_obj):
    tgt = j_obj
    for search in input().split('.'):
        search = search.replace('\\', '`').replace('\"', '~')
        try:
            tgt = tgt[search]
        except:
            print('NOTEXIST')
            return
    if isinstance(tgt, str):
        print('STRING' + ' ' + tgt.replace('`', '\\').replace('~', '\"'))
    else:
        print('OBJECT')


n, m = eval(input().replace(' ', ','))
j_string = ""
for i in range(n):
    j_string = j_string + input()
j_string = j_string.replace('\\\\', '`').replace('\\\"', '~')
j_obj = json.loads(j_string)
for i in range(m):
    find(j_obj)
