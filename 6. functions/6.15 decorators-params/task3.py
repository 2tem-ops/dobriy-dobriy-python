from functools import wraps


def tag_wrap(tag: str = "h1"):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"

        return wrapper

    return decorator


@tag_wrap(tag="div")
def lowercase(s: str) -> str:
    return s.lower()


print(lowercase(input()))
