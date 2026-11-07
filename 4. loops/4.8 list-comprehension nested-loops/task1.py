n = int(input())

matrix = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

for row in matrix:
    print(*row)