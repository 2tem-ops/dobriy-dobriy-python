lst_in = list(map(str.strip, __import__("sys").stdin.readlines()))

z = [i.split(": ") for i in lst_in]

d = {}

for author, book in z:
    d.setdefault(author, set())
    d[author].add(book)