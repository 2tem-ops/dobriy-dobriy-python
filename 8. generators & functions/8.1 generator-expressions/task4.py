a = int(input())

gen1 = (abs(x) for x in range(-a, a))
gen2 = (x ** 3 for x in gen1)

for _ in range(4):
    print(next(gen2), end=" ")