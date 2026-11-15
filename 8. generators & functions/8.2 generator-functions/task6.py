from typing import Generator, Iterable


def length_email(emails: Iterable[str], min_length: int = 5) -> Generator[str, None, None]:
    return (email for email in emails if email.startswith("@")
            or len(email[:email.find("@")]) >= min_length)


def rus_domain(gen_func: Generator[str, None, None]) -> Generator[str, None, None]:
    return (email for email in gen_func if email.endswith(".ru"))


length_gen = length_email(input().split(), min_length=10)
results = list(rus_domain(length_gen))

print(*results)
