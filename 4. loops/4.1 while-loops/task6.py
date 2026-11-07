total = 1
num = int(input())

while num > 0:
    total *= num % 10
    num //= 10

print(total)