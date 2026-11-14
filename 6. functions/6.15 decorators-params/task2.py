from functools import wraps


def start_value(start: int = 0):
    def deco(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            return start + func(*args, **kwargs)

        return wrapper

    return deco


@start_value(start=5)
def sum_nums(s: str) -> int:
    return sum(map(int, s.split()))


print(sum_nums(input()))
