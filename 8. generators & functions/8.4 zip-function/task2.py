lst_in = list(map(str.strip, __import__("sys").stdin.readlines()))

table = zip(*zip(*[lst.split() for lst in lst_in]))

for row in table:
    print(*row)