from math import isqrt

def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, int(input())):
    if is_prime(i):
        print(i, end=" ")