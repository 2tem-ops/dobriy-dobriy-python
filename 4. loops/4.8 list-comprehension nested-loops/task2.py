import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

res = sum(lst_in, [])

res.reverse()

print(*res)