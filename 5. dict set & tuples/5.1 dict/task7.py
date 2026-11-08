cache = {}

while num := int(input()):
    if num not in cache:
        cache[num] = round(num ** 0.5, 2)
        print(cache[num])
    else:
        print(f"значение из кэша: {cache[num]}")