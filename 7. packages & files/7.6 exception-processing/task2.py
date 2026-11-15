success_open_file, success_file_operations = True, True

try:
    with open("images/targets.dat", "r", encoding="utf-8") as file:
        last_row = file.readlines()[-1]
except FileNotFoundError:
    success_open_file = False
except:
    success_file_operations = False

