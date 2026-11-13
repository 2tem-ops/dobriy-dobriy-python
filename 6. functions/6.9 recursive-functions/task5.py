def get_line_list(d: list, a: list | None = None) -> list:
    if a is None:
        a = []

    for item in d:
        if isinstance(item, list):
            get_line_list(item, a)
        else:
            a.append(item)

    return a


d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]