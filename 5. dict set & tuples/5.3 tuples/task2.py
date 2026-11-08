lst = tuple(input().split())
print(*lst + ("Москва",) if "Москва" not in lst else lst)