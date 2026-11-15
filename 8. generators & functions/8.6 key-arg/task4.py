lst_in = list(map(str.strip, __import__("sys").stdin.readlines()))

t = tuple([tuple(int(j) if j.isdigit() else j for j in i.split(";")) for i in lst_in])
t_sorted = tuple(zip(*sorted(list(zip(*t)), key=lambda x: "Имя;Зачет;Оценка;Номер".find(x[0]))))