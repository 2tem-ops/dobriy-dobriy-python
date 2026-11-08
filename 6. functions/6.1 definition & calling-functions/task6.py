def check_email(email: str) -> None:
    print("ДА" if all(("@" in email, "." in email, email.isascii(), "!" not in email)) else "НЕТ")


check_email(input())