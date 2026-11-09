def get_nod(a: int, b: int) -> int:
    if a < b:
        a, b = b, a

    while b:
        a, b = b, a % b

    return a

print(get_nod(2, 1001))