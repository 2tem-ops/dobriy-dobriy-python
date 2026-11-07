s = iter(input())
res = ""

while " " not in res:
    res += next(s)

print(res)