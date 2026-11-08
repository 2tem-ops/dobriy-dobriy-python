lst = tuple(map(int, input().split()))
res = []

for digit in lst:
    if digit not in res:
        res.append(digit)

print(*tuple(res))