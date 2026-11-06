lst = list(map(int, input().split()))
lst.append(lst.pop() % 2 != 0)
print(*lst)