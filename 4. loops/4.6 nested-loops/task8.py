n = int(input())
res = []

for i in [64, 32, 16, 8, 4, 2, 1]:
    while n - i >= 0:
        n -= i
        res.append(i)

print(*res)
