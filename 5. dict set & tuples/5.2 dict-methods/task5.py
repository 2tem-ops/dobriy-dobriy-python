things = dict(sorted({k: v / 1000 for k, v in {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}.items()}.items(), key=lambda x: x[1], reverse=True))

kg = int(input())
res = ""

for k, v in things.items():
    kg = round(kg, 2)
    if kg - v >= 0:
        kg -= v
        res += k + " "

print(res)