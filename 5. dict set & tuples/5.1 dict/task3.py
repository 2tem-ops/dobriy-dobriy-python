cities = {k: v for k, v in [key.split("=") for key in input().split()]}

print("ДА" if 'house' in cities and 'True' in cities and '5' in cities else "НЕТ")