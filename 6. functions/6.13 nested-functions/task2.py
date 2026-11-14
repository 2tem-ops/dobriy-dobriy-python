def counter_add(n: int):

    def add(count: int = 0) -> int:
        count += n
        return count

    return add

cnt = counter_add(2)
print(cnt(int(input())))