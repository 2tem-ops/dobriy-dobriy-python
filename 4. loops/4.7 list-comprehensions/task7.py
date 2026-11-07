from functools import reduce

print(*[sum(pair) for pair in zip(map(int, input().split()), map(int, input().split()))])
