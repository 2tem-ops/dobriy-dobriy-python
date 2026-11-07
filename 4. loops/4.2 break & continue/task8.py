import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

print(*[i for i in lst_in if len(i.split()) == 1])