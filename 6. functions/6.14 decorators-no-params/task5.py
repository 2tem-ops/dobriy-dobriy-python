from functools import wraps


def group_words(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        keys, values = func(*args, **kwargs)
        return dict(zip(keys, values)).items()

    return wrapper


@group_words
def words_to_lists(w1: str, w2: str) -> tuple[list[str], list[str]]:
    return w1.split(), w2.split()


print(*sorted(words_to_lists(input(), input())))
