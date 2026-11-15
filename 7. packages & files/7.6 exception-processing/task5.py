try:
    with open("python/course_text.txt", "r", encoding="windows-1251") as file:
        pos = 0
        for line in file:
            line = line.lower()

            if "python" in line:
                pos += line.index("python")
                file.seek(pos)
                break
            pos += len(line)

except FileNotFoundError:
    pass