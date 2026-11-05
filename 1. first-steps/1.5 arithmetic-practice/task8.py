from math import sqrt, degrees, acos

x0, y0, x1, y1 = map(float, input().split())

cos_a = (x0 * x1 + y0 * y1) / (sqrt(x0 ** 2 + y0 ** 2) * sqrt(x1 ** 2 + y1 ** 2))
alpha = round(degrees(acos(cos_a)), 1)