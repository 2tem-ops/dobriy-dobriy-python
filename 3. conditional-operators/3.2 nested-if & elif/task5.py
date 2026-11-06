a, b, c = map(int, input().split())
sides = {a, b, c}

if a + b > c and a + c > b and b + c > a:
    match len(sides):
        case 1:
            print("Равносторонний треугольник")
        case 2:
            print("Равнобедренный треугольник")
        case 3:
            print("Разносторонний треугольник")
else:
    print("Это не треугольник")
