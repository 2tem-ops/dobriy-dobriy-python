def tag_html(text: str, tag: str = "h1", up: bool = True) -> str:
    if up: return f"<{tag.upper()}>{text}</{tag.upper()}>"
    return f"<{tag}>{text}</{tag}>"

print(tag_html(t:=input(), tag="div"), tag_html(t, tag="div", up=False), sep="\n")