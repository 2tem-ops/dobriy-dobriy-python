def fact_rec(n: int) -> int:
    if n <= 1:
        return 1
    return fact_rec(n - 1) * n

print(fact_rec(6))