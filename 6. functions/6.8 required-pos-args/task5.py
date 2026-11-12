def parser_data(text: str, /, max_count: int = 0, *, ignore_sign: bool = False) -> list[str]:
    text = [i for i in text if i in "0123456789-+.(); "]
    max_count = len(text) if not max_count else max_count

    for idx, char in enumerate(text):
        if char in "-+" and text[idx + 1] in "-+":
            del text[idx]

    res = [i for i in "".join(text).replace("-", " -").replace("+", " +").replace(".", " ").replace("(", " ").replace(")", " ").replace(";", " ").split()[:max_count] if i != ""]

    return [j for j in [i.replace("+", "").replace("-", "") for i in res] if j != ""] if ignore_sign else res


data_text = input()
result = parser_data(data_text, max_count=5, ignore_sign=True)