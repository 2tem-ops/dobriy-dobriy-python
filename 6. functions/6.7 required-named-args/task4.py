def count_chars(s: str, chars: str, *, return_type=tuple, ignore_case: bool = True):
    chars = chars.lower() if ignore_case else chars
    s = s.lower() if ignore_case else s

    count = {}

    for char in chars:
        for i in s:
            count[char] = [count.get(char, 0) + 0, count.get(char, 0) + 1][char in i]

    return return_type(count.values())

result = count_chars(input(), input(), return_type=set, ignore_case=False)
