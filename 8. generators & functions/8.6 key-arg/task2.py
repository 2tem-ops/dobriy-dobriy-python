lst_in = dict([[int(i) if i.isdigit() else i for i in lst.split("=")] for lst in list(map(str.strip, __import__("sys").stdin.readlines()))])

print(*[lst[0] for lst in sorted(lst_in.items(), key=lambda x: x[1], reverse=True)])
