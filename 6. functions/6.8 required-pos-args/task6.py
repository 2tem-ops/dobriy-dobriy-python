from math import sqrt


def is_right_rect(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int], d: tuple[int, int], /, *, precision: float = 0.001) -> bool:
    ab = (b[0] - a[0], b[1] - a[1])
    bc = (c[0] - b[0], c[1] - b[1])
    cd = (d[0] - c[0], d[1] - c[1])
    da = (a[0] - d[0], a[1] - d[1])

    len_ab = sqrt((ab[0] ** 2 + ab[1] ** 2))
    len_bc = sqrt((bc[0] ** 2 + bc[1] ** 2))
    len_cd = sqrt((cd[0] ** 2 + cd[1] ** 2))
    len_da = sqrt((da[0] ** 2 + da[1] ** 2))

    sab = ab[0] * bc[0] + ab[1] * bc[1]
    sbc = bc[0] * cd[0] + bc[1] * cd[1]
    scd = cd[0] * da[0] + cd[1] * da[1]
    sda = da[0] * ab[0] + da[1] * ab[1]

    cos_b = sab / (len_ab * len_bc)
    cos_c = sbc / (len_bc * len_cd)
    cos_d = scd / (len_cd * len_da)
    cos_a = sda / (len_da * len_ab)

    return (abs(cos_a) <= precision and
            abs(cos_b) <= precision and
            abs(cos_c) <= precision and
            abs(cos_d) <= precision)


rect_coords = [(float(x.split('=')[0]), float(x.split('=')[1])) for x in input().split()]
result = is_right_rect(*rect_coords)