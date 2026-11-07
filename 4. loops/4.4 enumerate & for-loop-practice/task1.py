text = input()
indexes = [text.find('ра')]

for i in text:
    found = text.find('ра', indexes[-1] + 1)
    if found == -1:
        break
    indexes.append(found)

print(*indexes)
