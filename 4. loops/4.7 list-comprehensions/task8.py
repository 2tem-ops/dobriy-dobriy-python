cities = input().split()

print([[cities[i], int(cities[i + 1])] for i in range(0, len(cities) - 1, 2)])