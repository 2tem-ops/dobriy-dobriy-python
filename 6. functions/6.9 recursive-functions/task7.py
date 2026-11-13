# compare elements at pointers
# add smaller element into result
# move pointer that found smaller element forward

def merge_lists(l1: list[int], l2: list[int]) -> list[int]:
    """
    compare elements at pointers
    add smaller element into result
    move pointer that found smaller element forward
    """

    res = []
    i, j = 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1

    res.extend(l1[i:] + l2[j:])

    return res


def recursive_merge_lists(l1: list[int], l2: list[int], acc: list[int] | None = None ) -> list[int]:
    if acc is None:
        acc = []

    if not l1 or not l2:
        acc.extend(l1 + l2)
        return acc

    if l1[0] <= l2[0]:
        acc.append(l1[0])
        return recursive_merge_lists(l1[1:], l2, acc)
    else:
        acc.append(l2[0])
        return recursive_merge_lists(l1, l2[1:], acc)


def merge_sort(lst: list[int]) -> list[int]:
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge_lists(left, right)

print(*merge_sort(list(map(int, input().split()))))


