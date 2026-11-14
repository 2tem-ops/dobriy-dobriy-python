from functools import wraps


def precision_deco(dx: float | int = 0.001):
    def deco(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * dx

        return wrapper

    return deco


@precision_deco(dx=0.5)
def area_by_sin(side1: int | float, side2: int | float, sin: float) -> float:
    return 1/2 * (side1 * side2 * sin)

print(area_by_sin(5, 5, 0.5))