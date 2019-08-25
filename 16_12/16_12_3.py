p = int(input())
auths = dict()
for i in range(p):
    ipt = input().lstrip().split(':')
    auths[ipt[0]] = -1 if len(ipt) == 1 else int(ipt[1])
r = int(input())
roles = dict()
for i in range(r):
    ipt = input().lstrip().split(' ')
    roles[ipt[0]] = dict()
    for auth in ipt[2:]:
        ipt_ = auth.split(':')
        if len(ipt_) == 1:
            roles[ipt[0]][ipt_[0]] = -1
        else:
            if ipt_[0] in roles[ipt[0]]:
                roles[ipt[0]][ipt_[0]] = max(
                    int(ipt_[1]), roles[ipt[0]][ipt_[0]])
            else:
                roles[ipt[0]][ipt_[0]] = int(ipt_[1])
u = int(input())
users = dict()
for i in range(u):
    ipt = input().lstrip().split(' ')
    users[ipt[0]] = dict()
    for role in ipt[2:]:
        for auth, lv in roles[role].items():
            if auth in users[ipt[0]]:
                users[ipt[0]][auth] = max(users[ipt[0]][auth], lv)
            else:
                users[ipt[0]][auth] = lv

q = int(input())
for i in range(q):
    user, ipt = input().rstrip().split(' ')
    ipt = ipt.split(':')
    auth = ipt[0]
    lv = -1 if len(ipt) == 1 else int(ipt[1])
    if user not in users:
        print('false')
    else:
        if auth not in users[user]:
            print('false')
        else:
            if lv == -1 and users[user][auth] == -1:
                print('true')
            elif lv == -1 and users[user][auth] != -1:
                print(users[user][auth])
            elif lv != -1 and users[user][auth] >= lv:
                print('true')
            else:
                print('false')
