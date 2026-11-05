x0, y0, x1, y1, x, y = map(int, input().split())

is_into_rect = x0 < x < x1 and y0 < y < y1
is_not_into_rect = not is_into_rect