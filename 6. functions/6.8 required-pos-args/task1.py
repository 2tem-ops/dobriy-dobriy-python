def is_right_tr(a: int | float, b: int | float, c: int | float, /, precision: float = 0.001) -> bool:
    return any([abs(c ** 2 - (a ** 2 + b ** 2)) < precision,
               abs(a ** 2 - (b ** 2 + c ** 2)) < precision,
               abs(b ** 2 - (a ** 2 + c ** 2)) < precision])

side_a, side_b, side_c = map(float, input().split())
result = is_right_tr(side_a, side_b, side_c)
