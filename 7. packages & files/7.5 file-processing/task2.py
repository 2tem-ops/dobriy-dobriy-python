with open("sites/links.txt", "r", encoding="windows-1251") as f_inp:
    f_inp.seek(0, 2)
    size_file = f_inp.tell()
