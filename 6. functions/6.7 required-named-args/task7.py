def are_anagrams(s1: str, s2: str, *, start=0, end=-1, ignore_case=True) -> bool:
    s1, s2 = [s1[start:end], s1[start:]][end == -1], [s2[start:end], s2[start:]][end == -1]
    return sorted([s1, s1.lower()][ignore_case]) == sorted([s2, s2.lower()][ignore_case])

result = are_anagrams(*(words := input().split()), ignore_case=False)