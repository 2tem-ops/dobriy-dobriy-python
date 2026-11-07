nums = list(map(int, input().split()))
n = len(nums)

for j in range(n - 1):
    swapped = False

    for i in range(n - 1 - j):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            swapped = True

    if not swapped:
        break

print(*nums)