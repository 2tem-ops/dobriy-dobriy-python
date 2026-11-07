bank = 1000
n = int(input())

while n > 0:
    bank += (bank * 0.05)
    n -= 1

print(round(bank, 2))