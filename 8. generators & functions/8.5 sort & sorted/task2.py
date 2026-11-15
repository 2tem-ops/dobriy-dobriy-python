def get_sort(d: dict[str, str]) -> list[str]:
    return [i[-1] for i in sorted(d.items(), key=lambda x: x[0], reverse=True)]