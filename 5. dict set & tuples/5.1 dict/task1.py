d = dict([key.split("=") for key in input().split()])

print(*sorted({k: int(v) for k, v in d.items()}.items()))