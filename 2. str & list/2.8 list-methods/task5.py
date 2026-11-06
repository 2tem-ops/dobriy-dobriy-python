nums = list(map(int, input().split()))

print(*sorted([nums.pop(nums.index(min(nums))) for _ in range(3)]))
