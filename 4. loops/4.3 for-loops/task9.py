n = int(input())

for i in range(1, n // 2):
    if n <= 1:
        print("НЕТ")
        break
    if n <= 3:
        print("ДА")
        break
    if n % 3 == 0 or n % 2 == 0:
        print("НЕТ")
        break
    if i != 1 and i != n:
        if n % i == 0:
            print("НЕТ")
            break
else:
    print("ДА")