n = int(input())
print(*([1] + [i for i in range(2, n // 2 + 1) if n % i == 0] + [n]) if n != 1 else [1])