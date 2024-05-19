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
    total = f"{color[colors[0]]}{color[colors[1]]}{'0'*color[colors[2]]}"
    notZeros = total[0 : total.index(0)]
    zeros = len(total[total.index("0") :])
    sufix = "kiloohms" if zeros >= 3 and zeros < 6 else "gigaohms"
    print(f"total of {zeros}")

    return f"{notZeros}"
