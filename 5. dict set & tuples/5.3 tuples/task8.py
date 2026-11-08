import sys

lst_in = tuple(tuple(pair.split()) for pair in list(map(str.strip, sys.stdin.readlines())))

print(lst_in)