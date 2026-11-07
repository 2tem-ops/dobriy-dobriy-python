x = int(input())
km = 10
count = 1

while True:
    if x == 10:
        print(2)
        break
    if km >= x:
        print(count)
        break
    km += (km / 10)
    count += 1