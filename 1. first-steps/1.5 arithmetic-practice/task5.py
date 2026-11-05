a, b, c = map(int, input().split())

sq_tr = __import__("math").sqrt((p := (a + b + c) / 2) * (p - a) * (p - b) * (p - c))