from typing import Generator


def moving_average(data: list[int] | tuple[int, ...], window_size: int = 3) -> Generator[float, None, None]:
    for i in range(len(data) - window_size + 1):
        yield sum(data[i:i + window_size]) / window_size


data = tuple(map(int, input().split()))
ws = int(input())

results = list(moving_average(data, ws))
