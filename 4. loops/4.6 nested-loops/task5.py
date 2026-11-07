import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
flag = True

for i in range(5):
    for j in range(5):
        if lst_in[i][j] != lst_in[j][i]:
            flag = False
            break
    if not flag:
        break

print("ДА" if flag else "НЕТ")