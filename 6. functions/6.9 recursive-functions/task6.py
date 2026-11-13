def get_path(N: int, c: list[int] = [1, 2]) -> int:
    if N <= 2:
        return N

    if len(c) < N:
        c.append(c[-1] + c[-2])
        get_path(N, c)
    return c[-1]

print(get_path(int(input())))
