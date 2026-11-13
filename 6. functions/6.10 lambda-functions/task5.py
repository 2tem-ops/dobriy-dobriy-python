def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

results = [
    filter_lst(digs := list(map(int, input().split()))),
    filter_lst(digs, key=lambda x: x < 0),
    filter_lst(digs, key=lambda x: x >= 0),
    filter_lst(digs, key=lambda x: x in (3, 4, 5))
]

print(*(" ".join(map(str, res)) for res in results), sep="\n")