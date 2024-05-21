def resistor_label(colors):
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

    if len(colors) == 1:
        return "0 ohms"

    tolerance = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%",
    }

    res, num = f" ±{tolerance[colors[-1]]}", ""

    for index, item in enumerate(colors):
        if index < len(colors) - 2:
            num = f"{num}{color[item]}"

    zeros = f"{'0'*color[colors[-2]]}"
    num = int(f"{num}{zeros}")

    if num >= 999999999:
        res = f"{num / 1000000000} gigaohms{res}"
    elif num >= 999999:
        res = f"{num / 1000000} megaohms{res}"
    elif num >= 999:
        res = f"{num / 1000} kiloohms{res}"
    else:
        res = f"{num} ohms{res}"

    return res.replace(".0 ", " ")
