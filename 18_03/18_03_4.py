# 判定胜利方
def win(state):
    if state[0] == state[1] == state[2] != 0:
        return state[0]
    elif state[3] == state[4] == state[5] != 0:
        return state[3]
    elif state[6] == state[7] == state[8] != 0:
        return state[6]
    elif state[0] == state[3] == state[6] != 0:
        return state[0]
    elif state[1] == state[4] == state[7] != 0:
        return state[1]
    elif state[2] == state[5] == state[8] != 0:
        return state[2]
    elif state[0] == state[4] == state[8] != 0:
        return state[0]
    elif state[2] == state[4] == state[6] != 0:
        return state[2]
    else:
        return 0


# 记忆
def cp2mem(state, score, player, mem):
    if tuple(state) not in mem:
        mem[tuple(state)] = score
        # 对称复制
        state_cp = state[:]
        state_cp[0], state_cp[1], state_cp[2] = state[6], state[7], state[8]
        state_cp[6], state_cp[7], state_cp[8] = state[0], state[1], state[2]
        mem[tuple(state_cp)] = score

        state_cp = state[:]
        state_cp[0], state_cp[3], state_cp[6] = state[2], state[5], state[8]
        state_cp[2], state_cp[5], state_cp[8] = state[0], state[3], state[6]
        mem[tuple(state_cp)] = score

        state_cp = state[:]
        state_cp[0], state_cp[1], state_cp[3] = state[8], state[5], state[7]
        state_cp[8], state_cp[5], state_cp[7] = state[0], state[1], state[3]
        mem[tuple(state_cp)] = score

        state_cp = state[:]
        state_cp[1], state_cp[2], state_cp[5] = state[3], state[6], state[7]
        state_cp[3], state_cp[6], state_cp[7] = state[1], state[2], state[5]
        mem[tuple(state_cp)] = score


def slt(state, player, mem):
    if tuple(state) in mem:
        return mem[tuple(state)]

    w_player = win(state)
    if w_player != 0:
        score = state.count(0) + 1 if w_player == 1 else - state.count(0) - 1
        mem[tuple(state)] = score
        return score
    if state.count(0) == 0:
        mem[tuple(state)] = 0
        return 0

    best_score = -10 if player == 1 else 10
    for i in range(9):
        if state[i] == 0:
            state_cp = state[:]
            state_cp[i] = player
            score = slt(state_cp, 1 if player == 2 else 2, mem)
            best_score = max(best_score, score) if player == 1 else min(
                best_score, score)
    cp2mem(state, best_score, player, mem)
    return best_score


t = int(input())
mem = dict()
for i in range(t):
    state = []
    for j in range(3):
        s = eval('[' + input().replace(' ', ',') + ']')
        state += s
    print(slt(state, 1, mem))
