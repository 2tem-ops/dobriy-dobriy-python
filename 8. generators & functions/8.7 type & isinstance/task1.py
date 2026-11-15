def get_add(a: str | int | float, b: str | int | float) -> str | int | float | None:
    return None if (type(a) in (float, int)) != (type(b) in (float, int)) else a + b