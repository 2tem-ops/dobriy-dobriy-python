def get_rect_value(length: int, width: int, tp: int = 0) -> int:
    if tp: return width * length
    return 2 * (width + length)