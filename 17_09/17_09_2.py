n, k = [int(it) for it in input().split(' ')]

events = dict()
keys = [it + 1 for it in range(n)]
for i in range(k):
    w, s, c = [int(it) for it in input().split(' ')]
    if s not in events:
        events[s] = ([], [])
    if s + c not in events:
        events[s + c] = ([], [])
    events[s][0].append(w)
    events[s + c][1].append(w)

for time, event in sorted(list(events.items())):
    for key in sorted(event[1]):
        keys[keys.index(-1)] = key
    for key in event[0]:
        keys[keys.index(key)] = -1

print(' '.join([str(it) for it in keys]))
