from functools import wraps


def sum_list(func):

    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        return sum(func(*args, **kwargs))

    return wrapper


@sum_list
def get_list(nums: str) -> list[int]:
    """Функция для формирования списка целых значений"""

    return list(map(int, nums.split()))
