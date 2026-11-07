pascal = []

for i in range(n:=int(input())):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = pascal[i-1][j-1] + pascal[i-1][j]

    pascal.append(row)

for row in pascal:
    print(*row)
