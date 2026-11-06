match withdraw := int(input()):
    case c if withdraw > 410123:
        print("Недостаточно средств")
    case c if withdraw > 50000:
        print("Превышен лимит разовой выдачи средств")
    case c if withdraw % 100 != 0:
        print("Ошибка: введите сумму кратную 100")
    case _:
        print(f"Выдано: {withdraw} руб.")