from itertools import count
from typing import Generator


def generate_primes() -> Generator[int, None, None]:
    numbers = count(2)
    while True:
        prime = next(numbers)
        yield prime
        numbers = filter(lambda x, p=prime: x % p != 0, numbers)


primes = generate_primes()
print(*[next(primes) for _ in range(20)])
