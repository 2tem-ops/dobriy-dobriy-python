def get_list_dig(lst: list | tuple | set) -> list[int]:
    return list(filter(lambda x: type(x) in (int, float), lst))