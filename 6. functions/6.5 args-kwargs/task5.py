def str_min(s1: str, s2: str) -> str:
    return min(s1, s2)


def str_min3(s1: str, s2: str, s3: str) -> str:
    return min(s3, str_min(s1, s2))


def str_min4(s1: str, s2: str, s3: str, s4: str) -> str:
    return min(s4, str_min3(s1, s2, s3))