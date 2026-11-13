lst_in = list(map(str.strip, __import__("sys").stdin.readlines()))

lst2D = list(map(lambda x: [int(i) for i in x.split()], lst_in))