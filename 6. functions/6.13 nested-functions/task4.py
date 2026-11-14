def tag_wrapper(tag: str):

    def wrap(text: str) -> str:
        return f"<{tag}>{text}</{tag}>"

    return wrap

tagger = tag_wrapper(input())
print(tagger(input()))