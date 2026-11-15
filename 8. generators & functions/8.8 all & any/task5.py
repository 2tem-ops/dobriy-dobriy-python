lst_in = list(map(str.strip, __import__("sys").stdin.readlines()))

def is_free(lst: list[list[str]]) -> bool:
    return any("#" in row for row in lst)

pole = [i.split() for i in lst_in]