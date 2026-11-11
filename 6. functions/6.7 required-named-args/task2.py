def operator(x: int, y: int, *, opt: str = "sum", initial: int = 0) -> int:
    if opt not in "summul":
        return 0
    return [x + y + initial, x * y * initial][opt == "mul"]

print((result := operator(*map(int, input().split()), opt="mul", initial=2)))