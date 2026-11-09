def tag_html(text: str, tag: str = "h1") -> str:
    return f"<{tag}>{text}</{tag}>"

print(tag_html(t:=input()), tag_html(t, tag="div"), sep="\n")