lst = tuple(map(int, input().split()))


for idx, dig in enumerate(lst):
    if lst.count(dig) > 1:
        print(idx, end=" ")