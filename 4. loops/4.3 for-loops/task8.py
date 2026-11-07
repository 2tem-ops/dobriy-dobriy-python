n = int(input())
divisors = []
large = []

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        divisors.append(i)
        if i != n // i:
            large.append(n // i)

print(*divisors + large[::-1], sep="\n")
