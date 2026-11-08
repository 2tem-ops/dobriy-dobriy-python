def stats(lst: list[int]) -> None:
    print(f"Min = {min(lst)}, max = {max(lst)}, sum = {sum(lst)}")


stats(list(map(int, input().split())))