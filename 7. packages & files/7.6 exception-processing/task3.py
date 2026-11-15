try:
    with open("bank.csv", "r", encoding="utf-8") as file:
        line1, line2 = file.readline().strip().split(","), file.readline().strip().split(",")
        row_data = dict(zip(line1, line2))
except FileNotFoundError:
    pass