with open("work_data/log_stats.txt", "a+", encoding="utf-8") as file:
    file.write(input())
    file.seek(0)
    header = file.readline()