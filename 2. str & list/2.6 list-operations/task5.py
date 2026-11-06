lst = [input() for _ in range(4)]
del lst[2]
lst[1] = "Пушкин"
lst[-1] = float(lst[-1]) * 2

print(lst)