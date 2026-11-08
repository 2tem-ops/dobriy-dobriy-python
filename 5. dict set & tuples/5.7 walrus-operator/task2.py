s = 0

while n := int(input()):
    if n % 2 != 0:
        continue
    s += n

print(s)