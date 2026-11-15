lst_in = list(map(str.strip, __import__("sys").stdin.readlines()))

print(*[i[0] for i in filter(lambda x: int(x[1]) > 500, tuple(tuple(lst.split("=")) for lst in lst_in))])