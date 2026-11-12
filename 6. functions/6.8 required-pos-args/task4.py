DEBUG = 10, 'DEBUG'
INFO = 20, 'INFO'
WARNING = 30, 'WARNING'
ERROR = 40, 'ERROR'
CRITICAL = 50, 'CRITICAL'


def log_event(timestamp: int, message: str, /, *, level: tuple[int, str] = INFO, format_log: str = "[%(time)] %(levelname) - %(message)") -> str | None:

    operations = {
        "%(time)": str(timestamp),
        "%(levelno)": str(level[0]),
        "%(levelname)": level[1],
        "%(message)": message
    }

    if level[0] >= INFO[0]:
        for placeholder, value in operations.items():
            format_log = format_log.replace(placeholder, value)

        return format_log

    return None


log_time = int(input())
log_msg = input()
log_item = log_event(log_time, log_msg, level=WARNING, format_log="%(levelname) - (%(time)) %(message)")

print(log_item)