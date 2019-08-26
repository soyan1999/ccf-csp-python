n = int(input())
battle_place = [[[0, 30]], [[0, 30]]]
attacker = battle_place[0]
defender = battle_place[1]
for i in range(n):
    op = input().rstrip()
    if op == 'end':
        t = attacker
        attacker = defender
        defender = t
    else:
        ops = op.split(' ')
        if len(ops) == 3:
            atk_num = int(ops[1])
            dfd_num = int(ops[2])
            attacker[atk_num][1] -= defender[dfd_num][0]
            defender[dfd_num][1] -= attacker[atk_num][0]
            if dfd_num != 0 and defender[dfd_num][1] <= 0:
                del defender[dfd_num]
            if attacker[atk_num][1] <= 0:
                del attacker[atk_num]
        else:
            attacker.insert(int(ops[1]), [int(ops[2]), int(ops[3])])

if battle_place[0][0][1] <= 0:
    print(-1)
elif battle_place[1][0][1] <= 0:
    print(1)
else:
    print(0)
for i in range(2):
    print(battle_place[i][0][1])
    print(' '.join([str(it) for it in
                    ([len(battle_place[i]) - 1] + [t[1] for t in battle_place[i][1:]])]))
