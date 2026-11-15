cities = input().split()
zipper = []

while cities:
    into = []
    for _ in range(3):
        if not cities:
            break
        into.append(cities.pop(0))
    zipper.append(into)

zipper = [i for i in zipper if len(i) == 3]

for row in zip(*zip(*zipper)):
    print(*row)