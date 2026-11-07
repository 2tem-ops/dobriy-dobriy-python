n, m = map(int, input().split())
i = n + 0 ** (n % 2)

while i <= m:
    print(i, end=" ")
    i += 2