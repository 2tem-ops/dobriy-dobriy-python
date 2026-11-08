import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

print(*sorted({int(k): v for k, v in [key.split("=") for key in lst_in]}.items()))