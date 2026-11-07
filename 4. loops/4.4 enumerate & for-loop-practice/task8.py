n = int(input())
matrix = [[0] * n for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

r = c = d = 0

for num in range(1, n * n + 1):
    matrix[r][c] = num

    nr, nc = r + dr[d], c + dc[d]

    if not (0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == 0):
        d = (d + 1) % 4
        nr, nc = r + dr[d], c + dc[d]

    r, c = nr, nc

for row in matrix:
    print(' '.join(str(num) for num in row))