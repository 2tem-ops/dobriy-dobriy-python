from typing import Generator


def balak_seq(max_len: int) -> Generator[int, None, None]:
    a, b, c = 1, 1, 1

    for _ in range(max_len):
        yield a
        a, b, c = b, c, a + b + c

seq = balak_seq(int(input()))

for i in seq:
    print(i, end=" ")