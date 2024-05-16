from math import sqrt


def score(x, y):
    hip = sqrt((x * x) + (y * y))

    if -1 <= hip <= 1:
        return 10
    elif -5 <= hip <= 5:
        return 5
    elif -10 <= hip <= 10:
        return 1
    else:
        return 0
