from functools import reduce

print(reduce(lambda x, y: x + y if y % 3 == 0 or y % 5 == 0 else x + 0, range(int(input())), 0))