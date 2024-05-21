def label(colors):
    color = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }
    total = int(f"{color[colors[0]]}{color[colors[1]]}{'0'*color[colors[2]]}")

    res = ""

    if total >= 999999999:
        res = f"{int(total/1000000000)} gigaohms"
    elif total >= 999999:
        res = f"{int(total /1000000)} megaohms"
    elif total >= 999:
        res = f"{int(total /1000)} kiloohms"
    else:
        res = f"{total} ohms"

    return res
