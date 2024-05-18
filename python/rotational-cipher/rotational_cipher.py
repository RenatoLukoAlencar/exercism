def rotate(text, key):
    letters, ntext = "abcdefghijklmnopqrstuvwxyz", ""

    for letter in text:
        if not letter.isalpha():
            ntext += letter
            continue

        nkey = letters.index(letter.lower()) + key
        nkey -= len(letters) if nkey >= len(letters) else 0
        ntext += letters[nkey] if letter.islower() else letters[nkey].upper()

    return ntext
