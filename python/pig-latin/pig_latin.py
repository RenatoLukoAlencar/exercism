def translate(text):
    arr = text.split(" ")
    print(f"arr: {arr}")
    vogalx = ["a", "e", "i", "o", "u", "x"]
    consoants = [
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "x",
        "y",
        "w",
        "z",
    ]

    for index, value in enumerate(arr):
        if value[0] in vogalx:
            arr[index] = f"{value}{'ay'}"
        else:
            arr[index] = f"{value[1:]}{value[0]}ay"

    return " ".join(arr)
