gen = (abs(x) for x in range(*map(int, input().split())))

for _ in range(5):
    print(next(gen))