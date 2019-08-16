n = int(input())

num_5 = n // 50
res_5 = n % 50
num_3 = res_5 // 30
res_3 = res_5 % 30
num_1 = res_3 // 10

print(num_5 * 7 + num_3 * 4 + num_1)
