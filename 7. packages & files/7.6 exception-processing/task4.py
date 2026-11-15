try:
    with open("logs/01-01-2025/log_app.txt", "r", encoding="utf-8") as log:
        log_errors = [line.strip() for line in log if "[ERROR]" in line]
except FileNotFoundError:
    pass