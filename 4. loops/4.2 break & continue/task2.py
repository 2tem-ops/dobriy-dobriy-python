prod = 1

while (num := int(input())) != 0:
    if num < 0:
        continue

    prod *= num

print(prod)