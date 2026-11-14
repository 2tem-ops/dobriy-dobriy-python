from functools import wraps


def process_symbols(chars="!?"):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            for char in chars:
                res = res.replace(char, "-")
            return res.replace("---", "-").replace("--", "-")

        return wrapper

    return decorator


@process_symbols(chars="?!:;,. ")
def latinize(s: str) -> str:
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    return s.lower().translate(str.maketrans(t)).replace(" ", "-")


print(latinize(input()))