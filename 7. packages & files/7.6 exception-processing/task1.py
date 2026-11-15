success_open_file = True

try:
    with open("diagnostics.csv", "r", encoding="utf-8") as file:
        header, row = file.readline(), file.readline()
except FileNotFoundError:
    success_open_file = False
