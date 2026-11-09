def check_password(password: str, chars: str = "$%!?@#") -> bool:
    return len(password) >= 8 and not (set(chars).isdisjoint(set(password)))

print(check_password('4364#'))
