try:
    with (open("lib/text_1", "r", encoding="utf-8") as text_1,
          open("lib/text_2", "r", encoding="utf-8") as text_2,
          open("text_all.txt", "w", encoding="windows-1251") as text_all):

        text_1_lines = text_1.readlines()[1:]
        text_2_lines = text_2.readlines()[1:]

        text_all.writelines(text_1_lines)
        text_all.write("\n")
        text_all.writelines(text_2_lines)
        
except FileNotFoundError:
    pass