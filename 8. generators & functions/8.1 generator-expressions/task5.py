from string import ascii_lowercase
from itertools import product

ltr_combs = ("".join(comb) for comb in list(product(ascii_lowercase, repeat=2)))

for _ in range(50):
    print(next(ltr_combs), end=" ")
