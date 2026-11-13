from math import sqrt

def is_right_rect(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int], d: tuple[int, int], /, *, precision: float = 0.001) -> bool:
    bd_diagonal_mid = (b[0] + d[0]) / 2, (b[1] + d[1]) / 2
    ac_diagonal_mid = (a[0] + c[0]) / 2, (a[1] + c[1]) / 2

    bd_diagonal_length = sqrt((d[0] - b[0]) ** 2 + (d[1] - b[1]) ** 2)
    ac_diagonal_length = sqrt((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2)

    return bd_diagonal_mid == ac_diagonal_mid and bd_diagonal_length == ac_diagonal_length

#rect_coords = [(float(x.split('=')[0]), float(x.split('=')[1])) for x in input().split()]

result = is_right_rect((3, 1), (6, 7), (10, 5), (7, -1))

print(result)

