def most_popular(people: list[str], *, case_sens: bool = False) -> tuple[str, int]:
    if case_sens:
        data = {person: people.count(person) for person in people}
    else:
        people = [p.lower() for p in people]
        data = {person: people.count(person) for person in people}

    maximum, res = 0, ""

    for item, value in data.items():
        if value > maximum:
            maximum = value
            res = item

    return res.lower(), maximum

writers = input().split()
result = most_popular(writers, case_sens=True)