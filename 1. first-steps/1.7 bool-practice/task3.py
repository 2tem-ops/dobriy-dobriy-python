a, b, c, d, x = map(float, input().split())

res_1 = a < x < b or c <= x <= d
res_2 = (x <= a or x >= b) and c <= x <= d
res_3 = (x <= a or x >= b) and (x < c or x > d)