def get_biggest_city(*args: str) -> str:
    return max(args, key=len)