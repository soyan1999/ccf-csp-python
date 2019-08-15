from datetime import datetime, timedelta

ins = input().split(' ')
n = int(ins[0])
s, t = ins[1], ins[2]
corns = []

for k in range(n):
    corn_ = input().split(' ')
    corn_[3] = corn_[3].lower().replace('jan', '1').replace('feb', '2').replace('mar', '3')\
        .replace('apr', '4').replace('may', '5').replace('jun', '6')\
        .replace('jul', '7').replace('aug', '8').replace('sep', '9')\
        .replace('oct', '10').replace('nov', '11').replace('dec', '12')
    corn_[4] = corn_[4].lower().replace('sun', '0').replace('mon', '1').replace('tue', '2')\
        .replace('wed', '3').replace('thu', '4').replace('fri', '5').replace('sat', '6')
    corn = []
    for i in range(5):
        its = set()
        if corn_[i] != '*':
            for it in corn_[i].split(','):
                if '-' in it:
                    bg, ed = int(it.split('-')[0]), int(it.split('-')[1])
                    for tt in range(bg, ed + 1):
                        its.add(tt)
                else:
                    its.add(int(it))
        corn.append(its)
    corn.append(corn_[5])
    corns.append(corn)


begin_day = datetime(int(s[:4]), int(s[4:6]), int(s[6:8]))
end_day = datetime(int(t[:4]), int(t[4:6]), int(t[6:8]))

mises = []
now = begin_day - timedelta(days=1)
while now < end_day:
    day_mis = []
    now += timedelta(days=1)
    for i in range(n):
        if len(corns[i][2]) != 0 and now.day not in corns[i][2]:
            continue
        elif len(corns[i][3]) != 0 and now.month not in corns[i][3]:
            continue
        elif len(corns[i][4]) != 0 and ((now.weekday()+1) % 7) not in corns[i][4]:
            continue
        else:
            hs = corns[i][1] if len(corns[i][1]) != 0 else set(
                [it for it in range(24)])
            ms = corns[i][0] if len(corns[i][0]) != 0 else set(
                [it for it in range(60)])
            for h in hs:
                for m in ms:
                    times = '%04d%02d%02d%02d%02d' % \
                        (now.year, now.month, now.day, h, m)
                    if now == begin_day or now == end_day:
                        if times < s or times >= t:
                            continue
                    day_mis.append((times, i, corns[i][5]))

    day_mis.sort()
    mises += day_mis

for mis in mises:
    print(mis[0]+' '+mis[2])
