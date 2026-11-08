cities = set()

while (city := input()) != "q":
    cities.add(city)

print(len(cities))