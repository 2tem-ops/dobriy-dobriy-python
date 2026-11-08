import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

hash_table = {}

for html in lst_in:
    if html not in hash_table:
        hash_table[html] = f"HTML-страница для адреса {html}"
        print(hash_table[html])
    else:
        print(f"Взято из кэша: {hash_table[html]}")
