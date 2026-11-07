from functools import reduce

print(reduce(lambda x, y: x + y if y % 2 != 0 else x + 0, map(int, input().split()), 0))