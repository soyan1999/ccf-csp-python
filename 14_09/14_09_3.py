sub_str = input().rstrip()
if_transform = True if input() == '1' else False
n = int(input())
for i in range(n):
    ss = input().rstrip()
    if if_transform:
        pr = sub_str in ss
    else:
        pr = sub_str.lower() in ss.lower()
    if pr:
        print(ss)
