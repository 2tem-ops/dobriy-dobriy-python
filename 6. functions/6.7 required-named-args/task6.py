def filter_by_length(*args, min_length: int = 0, max_length: int) -> list[str]:
    return [x for x in args if min_length <= len(x) <= max_length]


names_result = filter_by_length(*(names_initial := input().split()), min_length=5, max_length=9)