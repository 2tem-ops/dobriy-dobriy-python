from string import ascii_letters, digits

emails = input().split()
symbols = {*ascii_letters, *digits, "@", "_", "."}

for email in emails:
    disallowed = set(email) - symbols
    if all([not any(filter(disallowed.__contains__, email)), "." not in email[:email.find("@")]]):
        print(email, end=" ")