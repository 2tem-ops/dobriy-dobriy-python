import sys
s = sys.stdin.readlines()
lst2D = [list(map(int, x.strip().split())) for x in s]

for idx, row in enumerate(lst2D):
    if idx % 2 != 0:
        print(*row[::-1], end=" ")
    else:
        print(*row, end=" ")
