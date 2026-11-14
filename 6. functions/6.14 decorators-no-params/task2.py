from functools import wraps


def func_show(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Площадь прямоугольника: {func(*args, **kwargs)}")

    return wrapper


@func_show
def get_sq(width: int | float, height: int | float) -> int | float:
    return width * height
