def verify(lst2d: list[list[int]]) -> bool:
    n = len(lst2d)

    def is_isolate() -> bool:
        for i in range(1, n):
            for j in range(1, n):
                if lst2d[i - 1][j - 1] + lst2d[i - 1][j] + lst2d[i][j - 1] + lst2d[i][j]  > 1:
                    return False
        return True

    return is_isolate()