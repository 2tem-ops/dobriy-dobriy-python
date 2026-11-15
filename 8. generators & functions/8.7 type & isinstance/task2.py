from typing import Iterable


def get_sum(it: Iterable) -> int:
    return sum(filter(lambda x: type(x) is int, it))