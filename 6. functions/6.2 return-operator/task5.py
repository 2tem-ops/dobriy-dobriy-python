def is_odd(num: int) -> bool:
    return num % 2 != 0


print(*filter(is_odd, map(int, input().split())))