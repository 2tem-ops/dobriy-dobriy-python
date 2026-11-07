cities = input().split()

for i in range(len(cities) - 1):
    if cities[i + 1][0].lower() != cities[i][-1].strip("ъьы"):
        print("НЕТ")
        break
else:
    print("ДА")