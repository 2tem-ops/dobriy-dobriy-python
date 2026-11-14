with open("course.new.dat", "r", encoding="utf-8") as f_text:
    start_5 = f_text.read(5)
    f_text.seek(0, 2)
    f_text.seek(f_text.tell() - 5)
    end_5 = f_text.read(5)