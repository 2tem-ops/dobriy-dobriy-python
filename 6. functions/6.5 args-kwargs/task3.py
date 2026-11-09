def get_data_fig(*args, **kwargs) -> tuple:
    order = ["tp", "color", "closed", "width"]
    return (sum(args),) + tuple(kwargs[x] for x in order if x in kwargs)

print(get_data_fig(1, 2, 3, tp=True, color=False, closed="hello"))