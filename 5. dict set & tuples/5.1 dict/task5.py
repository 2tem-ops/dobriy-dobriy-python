numbers = input().split()

data = {k[:2]: [] for k in numbers}

for number in numbers: data[number[:2]].append(number)

print(*sorted(data.items()))