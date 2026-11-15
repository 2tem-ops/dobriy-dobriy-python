lst_in = [lst.split() for lst in list(map(str.strip, __import__("sys").stdin.readlines()))]

for row in zip(*lst_in):
    print(*row)