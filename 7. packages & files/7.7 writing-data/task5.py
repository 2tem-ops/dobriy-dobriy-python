try:
    with (open("lang_doc/python_base.dat", "r+", encoding="utf-8") as python_file,
        open("lang_doc/java_base.dat", "r+", encoding="utf-8") as java_file):
        data1, data2 = python_file.read(), java_file.read()

        python_file.seek(0); java_file.seek(0)
        python_file.write(data2); java_file.write(data1)

        python_file.truncate(); java_file.truncate()
except FileNotFoundError:
    pass