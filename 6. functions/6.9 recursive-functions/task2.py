nums = list(map(int, input().split()))

def get_rec_sum(lst_digits):
    if len(lst_digits) == 1:
        return lst_digits[0]
    return lst_digits[0] + get_rec_sum(lst_digits[1:])

print(get_rec_sum(nums))