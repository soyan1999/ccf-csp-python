def func(txts):  # 计算八位字符串异或值
    out = 0
    for txt in txts:
        out = out ^ eval('0x' + txt)
    return '%X' % (out,)


n, s, l = eval(input().replace(' ', ','))
disks = ['' for i in range(n)]
for i in range(l):
    num, txt = input().split(' ')
    disks[int(num)] = txt

max_num = len(disks[0]) // 8 * (n - 1)
m = int(input())
for i in range(m):
    num = int(input())
    if num >= max_num:
        print('-')
    else:
        addr_disk = num // (s * (n - 1)) * s + num % s  # 盘内偏移块数
        addr_c = num // (s * (n - 1))  # 层数
        addr_n = (num // s) % (n - 1)  # 层顺序
        addr_p = n - 1 - addr_c % n  # P区层偏移
        addr_d = addr_p + 1 + addr_n if addr_p + 1 + \
            addr_n < n else addr_n - (n - addr_p - 1)  # 层偏移
        if disks[addr_d] != '':
            print(disks[addr_d][addr_disk * 8:(addr_disk + 1) * 8])
        elif l >= n - 1:
            txts = []
            for i, txt in enumerate(disks):
                if i != addr_d:
                    txts.append(txt[addr_disk * 8:(addr_disk + 1) * 8])
            print(func(txts))
        else:
            print('-')
