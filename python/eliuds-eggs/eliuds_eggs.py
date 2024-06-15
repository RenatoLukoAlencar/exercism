from math import floor as f


def egg_count(display_value):
    b, c = "", display_value

    while c != 0:
        b += "1" if c % 2 != 0 else "0"
        c = f(c / 2)

    return b.count("1")
