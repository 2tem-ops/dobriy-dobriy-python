from math import prod

nums = zip(map(int, input().split()), map(int, input().split()))

for _ in range(3):
    print(prod(next(nums)), end=" ")