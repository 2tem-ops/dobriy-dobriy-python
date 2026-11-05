rect_width, rect_height, w, h = map(int, input().split())

total = (rect_width % w != 0) * (rect_height // h) + (rect_height % h != 0) * (rect_width // w) + (rect_width % w != 0 and rect_height % h != 0)

