from math import trunc

print(*(lst_res := [float(x) for x in input().split() if trunc(float(x)) % 2 == 0]))