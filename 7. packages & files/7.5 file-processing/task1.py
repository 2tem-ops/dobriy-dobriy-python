with open("log.dat", "r", encoding="utf-8") as f_log:
    header, *_, last_data = f_log.readlines()