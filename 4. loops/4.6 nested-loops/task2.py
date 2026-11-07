import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

for item in lst_in:
    item = item.split()
    print("-".join(item))
