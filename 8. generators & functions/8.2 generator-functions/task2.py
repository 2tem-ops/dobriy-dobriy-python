from typing import Generator

N = int(input())


def get_sum(total: int) -> Generator[int, None, None]:
    n = 1

    for i in range(2, total + 2):
        yield n
        n += i
