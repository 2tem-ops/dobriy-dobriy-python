match age := int(input()):
    case c if 0 <= age <= 2:
        print("Младенец")
    case c if 3 <= age <= 12:
        print("Ребенок")
    case c if 13 <= age <= 17:
        print("Подросток")
    case c if 18 <= age <= 64:
        print("Взрослый")
    case c if 64 <= age <= 120:
        print("Пенсионер")
    case _:
        print("Ошибка: некорректный возраст")