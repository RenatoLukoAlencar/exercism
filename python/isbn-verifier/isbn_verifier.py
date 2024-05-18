def is_valid(isbn):
    res, i = 0, 0
    for digit in str(isbn).replace("-", ""):
        if digit.isnumeric():
            res += (10 - i) * int(digit)
            i += 1
        elif digit == "X" and i == 9:
            res += (10 - i) * 10
            i += 1
        elif i != 9:
            return False

    return res % 11 == 0 and i == 10
