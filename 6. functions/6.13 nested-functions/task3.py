def tag_wrap():

    def tag(text: str) -> str:
        return f"<h1>{text}</h1>"

    return tag

tagger = tag_wrap()
print(tagger(input()))