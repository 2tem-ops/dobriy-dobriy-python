from typing import Generator


def counter(start: int = 0, step: int = 1) -> Generator[int, None, None]:
    while True:
        yield start
        start += step


start, step = map(int, input().split())
gen = counter(start=start, step=step)

for _ in range(3):
    print(next(gen), end=" ")
