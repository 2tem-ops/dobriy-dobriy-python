from functools import wraps


def sort_collection(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return sorted(func(*args, **kwargs))

    return wrapper


@sort_collection
def get_list(s: str) -> list[int]:
    return list(map(int, s.split()))


print(*get_list(input()))
