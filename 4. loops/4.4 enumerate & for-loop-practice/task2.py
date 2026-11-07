from re import match

res = match(r"^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$", input())

print("ДА" if res else "НЕТ")