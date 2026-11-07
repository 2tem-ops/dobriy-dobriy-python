n = int(input())
count = 1

while True:
    if count ** 2 > n:
        print(count)
        break
    count += 1