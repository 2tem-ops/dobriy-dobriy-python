def is_string(lst: list | tuple | set) -> bool:
    return all(map(lambda x: isinstance(x, str), lst))