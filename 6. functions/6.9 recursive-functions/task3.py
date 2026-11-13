N = int(input())

def fib_rec(N: int, f: list[int]) -> list[int]:
    if N > 2:
        f.append(f[-1] + f[-2])

    if len(f) < N:
        fib_rec(N, f)
    return f

result = fib_rec(N, [1, 1])