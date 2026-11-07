n = int(input())
s = 1
i = 2

while i <= n:
    s += 1/i
    i += 1

print(round(s, 3))