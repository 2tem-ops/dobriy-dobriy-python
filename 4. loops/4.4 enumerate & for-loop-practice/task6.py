nums = list(map(float, input().split()))
minimum = nums[0]

for num in nums:
    if num < minimum:
        minimum = num

print(minimum)