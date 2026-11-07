count = 1
n = int(input())
res = []

while count <= n:
    if n >= 100:
        print("слишком большое значение n")
        break

    if count % 3 == 0 and count % 5 == 0:
        res.append(count)

    count += 1
else:
    print(*res)
