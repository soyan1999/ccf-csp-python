n = int(input())
nums = eval('[' + input().replace(' ', ',') + ']')
nums.sort()

min_abs = 10000
for i in range(n - 1):
    min_abs = min(abs(nums[i] - nums[i + 1]), min_abs)

print(min_abs)
