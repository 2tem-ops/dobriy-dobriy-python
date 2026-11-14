with open("staff/persons.dat", "r", encoding="utf-8") as fp:
    for idx, line in enumerate(fp, start=1):
        if "Сергей" in line and "Балакирев" in line:
            num_person = idx
            break