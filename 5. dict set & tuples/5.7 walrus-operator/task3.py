def f(x):
    return abs(x) ** 0.5 + 3.2 + x


t = tuple(map(float, input().split()))

lst = [[y := f(x), y ** 2, y ** 3] for x in t]