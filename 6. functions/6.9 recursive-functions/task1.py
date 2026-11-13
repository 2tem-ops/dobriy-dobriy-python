def get_rec_N(N: int) -> None:
    if N > 1: get_rec_N(N - 1)
    print(N)

get_rec_N(int(input()))