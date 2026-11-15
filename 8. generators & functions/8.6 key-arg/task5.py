lst_in = list(map(str.strip, __import__("sys").stdin.readlines()))
ranks = {"рядовой": 0, "сержант": 1, "старшина": 2, "прапорщик": 3, "лейтенант": 4, "капитан": 5, "майор": 6, "подполковник": 7, "полковник": 8}

lst = sorted([i.split("=") for i in lst_in], key=lambda x: ranks[x[1]])



