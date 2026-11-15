a, b = map(int, input().split())

func_x = (round(0.5 * pow(x / 100, 2) - 2.0, 2) for x in range(100 * a, 100 * b + 1))

for _ in range(20):
    print(next(func_x), end=" ")
