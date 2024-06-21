def recite(start, take=1):
    dic = {
        "10": "ten",
        "9": "nine",
        "8": "eight",
        "7": "seven",
        "6": "six",
        "5": "five",
        "4": "four",
        "3": "three",
        "2": "two",
        "1": "one",
        "0": "no",
    }

    temp = [
        "# green bottle@ hanging on the wall,",
        "# green bottle@ hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be ! green bottle$ hanging on the wall.",
    ]

    res = []

    for turn in range(start, start - take, -1):
        for line in temp:
            current = line
            current = (
                current.replace(
                    "#", dic[str(turn)].capitalize()[:1] + dic[str(turn)][1:]
                )
                .replace("!", dic[str(turn - 1)])
                .replace("@", "s" if turn != 1 else "")
                .replace("$", "s" if turn - 1 != 1 else "")
            )
            res.append(current)

        res.append("")

    return res[:-1]
