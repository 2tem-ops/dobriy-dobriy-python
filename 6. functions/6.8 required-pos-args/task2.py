def verify_password(psw: str, /, chars: str = "@#!", min_length: int = 8) -> bool:
    return not set(chars).isdisjoint(psw) and len(psw) >= min_length and set(psw).isdisjoint("абвгдеёжзийклмнопрстуфхцчшщьыъэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ")


password = input()
result = verify_password(password, chars="0123456789", min_length=10)