from itertools import batched
from math import isqrt

nums = list(map(int, input().split()))

print([list(i) for i in list(batched(nums, isqrt(len(nums))))])