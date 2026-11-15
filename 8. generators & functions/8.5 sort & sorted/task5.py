lst_in = dict([[int(i) if i.isdigit() else i for i in lst.split(":")] for lst in list(map(str.strip, __import__("sys").stdin.readlines()))])

print(*sorted(lst_in, key=lst_in.get)[:3])