def decode(string):
    res, count = "", ""

    for letter in string:
        if letter.isnumeric():
            count += letter
        else:
            res += letter * int(count) if count != "" else letter
            count = ""

    return res

def encode(string):
    count, ll, res = 1, "", ""

    for letter in string + "#":
        if ll != letter:
            res += f"{count if count > 1 else ''}{ll}"
            count, ll = 0, letter
        count += 1
    return res