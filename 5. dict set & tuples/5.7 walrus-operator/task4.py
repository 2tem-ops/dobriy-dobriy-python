prod = 1

while (n := int(input())) > 0:
    if n % 3 != 0:
        continue

    prod *= n

print(prod)