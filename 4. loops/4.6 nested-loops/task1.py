n = int(input())
matrix = [[1] * (n - 1) + [5] for _ in range(n)]

for row in matrix:
    print(*row)