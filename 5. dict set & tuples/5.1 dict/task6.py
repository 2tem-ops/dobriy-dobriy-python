import sys

lst_in = [pair.split() for pair in list(map(str.strip, sys.stdin.readlines()))]

data = {v: [] for k, v in lst_in}

for number, name in lst_in:
    data[name].append(number)

print(*sorted(data.items()))

