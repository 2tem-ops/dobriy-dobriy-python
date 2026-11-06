x, y = map(float, input().split())

print({0: "I четверть", 1: "II четверть", 2: "III четверть", 3: "IV четверть"}[[x > 0 and y > 0, x < 0 and y > 0, x < 0 and y < 0, x > 0 and y < 0].index(True)])