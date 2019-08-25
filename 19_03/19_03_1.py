n = int(input())
list = eval('[' + input().replace(' ', ',') + ']')
max_num, min_num = (
    list[0], list[-1]) if list[0] > list[-1] else(list[-1], list[0])
if n % 2 == 0:
    mid = '%.1f' % ((list[n // 2] + list[n // 2 - 1]) / 2,)
    if mid[-1] == '0':
        mid = mid[0:-2]
else:
    mid = '%d' % (list[n // 2])

print(str(max_num)+' ' + mid+' '+str(min_num))
