vals = [3500, 4955, 7655, 11255, 30755, 44755, 61005, float('inf')]
taxs = [0, 3, 10, 20, 25, 30, 35, 45]
levels = [3500, 5000, 8000, 12500, 38500, 58500, 83500]

t = int(input())
for i in range(len(vals)):
    if vals[i] >= t:
        old_v = 0 if i == 0 else vals[i - 1]
        old_l = 0 if i == 0 else levels[i - 1]
        # t-old_v=(q-old_l//100)*(100-taxs[i])
        q = (t - old_v) // (100 - taxs[i]) + old_l // 100
        print(q * 100)
        break
