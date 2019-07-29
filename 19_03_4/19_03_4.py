# 根据通信对之一生成另一个的栈元素(proc_num, action)
def func(source, num):
    return (int(source[1:]), 'S' + str(num)) if source[0] == 'R' else (int(source[1:]), 'R' + str(num))


def solution(threads, n):
    for k, thread in enumerate(threads):
        stack = []  # 等待栈
        while len(thread) != 0:
            stack.append(func(thread.pop(), k))
            in_proc = {k}  # 等待集合
            while len(stack) != 0:
                wait_num = stack[-1][0]
                # 被等待进程为空，或已经在等待集合，判定发生死锁
                if len(threads[wait_num]) == 0 or wait_num in in_proc:
                    return 1
                # 被等待进程满足条件，出栈，并从等待集合移除序号
                if threads[wait_num][-1] == stack[-1][1]:
                    threads[wait_num].pop()
                    proc = int(stack.pop()[1][1:])
                    in_proc.remove(proc)
                # 被等待进程不满足条件，入栈，加入等待集合
                else:
                    stack.append(func(threads[wait_num].pop(), wait_num))
                    in_proc.add(int(stack[-1][1][1:]))
    return 0


t, n = eval(input().replace(' ', ','))
for i in range(t):
    threads = []  # 进程操作组
    for j in range(n):
        thread = input().split(' ')
        thread.reverse()
        threads.append(thread)
    print(solution(threads, n))
