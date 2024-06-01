TENMULT = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
LESS20 = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]


def _convert_hundreds(n):
    if n < 20:
        return LESS20[n]
    elif n < 100:
        return TENMULT[n // 10] + ("" if n % 10 == 0 else "-" + LESS20[n % 10])
    else:
        return (
            LESS20[n // 100]
            + " hundred"
            + ("" if n % 100 == 0 else " " + _convert_hundreds(n % 100))
        )


def _convert_thousands(n):
    words = ""
    if n >= 1000000000:
        words += _convert_hundreds(n // 1000000000) + " billion"
        n %= 1000000000
    if n >= 1000000:
        if words:
            words += " "
        words += _convert_hundreds(n // 1000000) + " million"
        n %= 1000000
    if n >= 1000:
        if words:
            words += " "
        words += _convert_hundreds(n // 1000) + " thousand"
        n %= 1000
    if n > 0:
        if words:
            words += " "
        words += _convert_hundreds(n)
    return words


def say(n):
    if 0 > n or 999999999999 < n:
        raise ValueError("input out of range")

    return _convert_thousands(n) if n != 0 else "zero"
