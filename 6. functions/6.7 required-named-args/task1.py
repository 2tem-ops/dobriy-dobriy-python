def get_params(x: int, y: int, *, flags=None, func) -> dict:
    return {"x": x, "y": y, "flags": flags, "func": func}

params = get_params(x=10, y=20, flags=True, func='abs')