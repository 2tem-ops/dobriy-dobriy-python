def check_phone(phone: str, format_phone: str = "8(xxx)xxx-xx-xx", /, format_symbol: str = "x") -> bool:
    if format_symbol not in format_phone or not phone.replace("(", "").replace(")", "").replace(" ", "").replace("-", "").replace("+", "").isalnum():
        #print("FIRST WRONG", phone.replace("(", "").replace(")", "").replace(" ", "").replace("-", ""), format_phone)
        return False

    if "+" in format_phone and "+" not in phone:
        return False

    phone = phone.replace("(", " (").replace(")", ") ").replace("-", " ").split()
    format_phone = format_phone.replace("(", " (").replace(")", ") ").replace("-", " ").split()

    if len(phone) != len(format_phone):
        #print(f"length {phone} {format_phone}")
        return False

    for i, sect in enumerate(format_phone):
        try:
            format_phone[i] = phone[i]
        except IndexError:
            #print(f"oopsie index {phone} {format_phone}")
            return False

    return phone == format_phone


phone_number = "8(951)432-5544"
result = check_phone(phone_number, "+7(***)*** ****", format_symbol="*")
print(result)