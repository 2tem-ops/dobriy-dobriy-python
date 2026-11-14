def counter_add():

    def add(counter: int):
        counter += 5
        return counter

    return add

cnt = counter_add()
print(cnt(int(input())))
