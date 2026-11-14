from functools import wraps
import time


def timeit(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            print(f'{func.__name__} executed in {elapsed} seconds')

    return wrapper


@timeit
def hey():
    time.sleep(3)
    print("hey")


hey()
