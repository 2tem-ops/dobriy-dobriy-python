lst_in = list(map(str.strip, __import__("sys").stdin.readlines()))

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}

lst_in = dict((*i.split("="),) for i in lst_in)

menu = {**menu, **lst_in}
