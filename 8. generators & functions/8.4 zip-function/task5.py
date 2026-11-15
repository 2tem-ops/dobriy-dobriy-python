s = input()
idx = [s.index(i) for i in s]

lst = [*zip(s, idx)]

if len(lst) > 10:
    lst = lst[:10]

