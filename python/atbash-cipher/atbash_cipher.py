PLAIN = "abcdefghijklmnopqrstuvwxyz"
CIPHER = list(reversed(PLAIN))


def encode(plain_text):
    newString, newArr = "", []
    for letter in plain_text.lower().replace(" ", ""):
        if letter.isnumeric():
            newString += letter
        elif letter in PLAIN:
            newString += CIPHER[PLAIN.index(letter)]

        if len(newString) == 5:
            newArr.append(newString)
            newString = ""

    newArr.append(newString) if newString != "" else None

    return " ".join(newArr)


def decode(ciphered_text):
    newString = ""
    for letter in ciphered_text.lower().replace(" ", ""):
        if letter.isnumeric():
            newString += letter
        elif letter in CIPHER:
            newString += PLAIN[CIPHER.index(letter)]

    return newString
