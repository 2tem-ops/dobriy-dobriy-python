n = int(input())
matrix = [[i] * n for i in range(n)]

for row in matrix:
    print(*row)