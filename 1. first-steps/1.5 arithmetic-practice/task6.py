a, b, alpha = map(float, input().split())

length_c = __import__("math").sqrt(a ** 2 + b ** 2 - 2 * a * b * __import__("math").cos(alpha))