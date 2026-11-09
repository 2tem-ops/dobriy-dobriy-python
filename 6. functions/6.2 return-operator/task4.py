def is_even(num: int) -> bool:
    return num % 2 == 0


while (x := int(input())) != 1:
    if is_even(x):
        print(x)