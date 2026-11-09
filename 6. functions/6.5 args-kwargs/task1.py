def get_even(*args: int) -> list[int]:
    return list(filter(lambda x: x % 2 == 0, args))