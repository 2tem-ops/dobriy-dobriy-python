cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]

gen = (cities[i % len(cities)] for j in range(1_000_000) for i in range(6) )

for _ in range(20):
    print(next(gen), end=" ")