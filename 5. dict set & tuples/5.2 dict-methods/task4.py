import sys

lst_in = [pair.split() for pair in list(map(str.strip, sys.stdin.readlines()))]

data = {}

for date, name in lst_in:
    data.setdefault(date, []).append(name)

for date, name in data.items():
    print(f"{date}: {", ".join(name)}")