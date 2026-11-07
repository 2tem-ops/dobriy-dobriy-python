import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
flag = True

for i in range(len(lst_in) - 1):
    for j in range(i, len(lst_in) - 1):
        if sum([lst_in[i][j], lst_in[i][j + 1], lst_in[i + 1][j], lst_in[i + 1][j + 1]]) > 1:
            flag = False
            break
    if not flag:
        break

print("ДА" if flag else "НЕТ")
