words = input().lower().split()

print({word: words.count(word) for word in words}.get("и", 0))