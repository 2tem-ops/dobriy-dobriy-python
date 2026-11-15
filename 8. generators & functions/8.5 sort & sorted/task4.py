lst1, lst2 = sorted(map(int, input().split())), sorted(map(int, input().split()), reverse=True)

print(*map(sum, zip(lst1, lst2)))