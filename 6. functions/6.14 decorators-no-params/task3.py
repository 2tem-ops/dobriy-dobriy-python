from functools import wraps


def show_menu(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        for idx, item in enumerate(res, start=1):
            print(f'{idx}. {item}')

    return wrapper


@show_menu
def get_menu(s: str) -> list[str]:
    return s.split()


menu = input()
get_menu(menu)
