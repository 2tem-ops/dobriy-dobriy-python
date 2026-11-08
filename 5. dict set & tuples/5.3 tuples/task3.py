cities = tuple(input().split())

print(*cities[:cities.index("Ульяновск")] + cities[cities.index("Ульяновск") + 1:] if "Ульяновск" in cities else cities)