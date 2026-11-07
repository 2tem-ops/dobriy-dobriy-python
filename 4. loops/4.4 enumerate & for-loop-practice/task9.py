expression = input().replace(" ", "").replace("+", " + ").replace("-", " - ").split()
if expression[0] == "-":
    expression = expression[1:]
    expression [0] = str(-int(expression[0]))
total = int(expression[0])
i = 0

while True:
    try:
        if expression[i + 1] == "+":
            total += int(expression[i + 2])
        elif expression[i + 1] == "-":
            total -= int(expression[i + 2])
    except IndexError:
        break
    i += 2

print(total)