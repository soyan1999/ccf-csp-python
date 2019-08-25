n = int(input())
ps = [int(it) for it in input().rstrip().split(' ')]

sets = [set() for i in range(5)]
sets[4] = set([i for i in range(20)])
for p in ps:
    enable = False
    mini = 100
    mini_set = 5
    for i in range(p - 1, 5):
        if len(sets[i]) != 0:
            enable = True
            min_in = min(sets[i])
            if mini > min_in:
                mini = min_in
                mini_set = i
    if enable:
        sets[mini_set].remove(mini)
        if mini_set - p >= 0:
            sets[mini_set - p].add(mini)
        begin = (mini + 1) * 5 - mini_set
        end = (mini + 1) * 5 - mini_set + p
        print(' '.join([str(it) for it in range(begin, end)]))
    else:
        adding = []
        for i in range(p):
            mini = 100
            mini_set = 5
            for j in range(p):
                if len(sets[j]) != 0:
                    min_in = min(sets[j])
                    if mini > min_in:
                        mini = min_in
                        mini_set = j
            sets[mini_set].remove(mini)
            if mini_set != 0:
                sets[mini_set - 1].add(mini)
            adding.append((mini + 1) * 5 - mini_set)
        print(' '.join([str(it) for it in adding]))
