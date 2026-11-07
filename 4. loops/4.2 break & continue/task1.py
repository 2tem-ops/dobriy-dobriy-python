p = [0] * 10
count = 0

while count < 5:
    index = int(input())
    if p[index] == 1:
        continue
    p[index] = 1
    count += 1

print(*p)