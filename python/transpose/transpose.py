def transpose(lines):
    splited, res = lines.split("\n"), []

    for indexw, word in enumerate(splited):
        for index, letter in enumerate(word):
            if len(res) < index + 1:
                res.append([])

            while len(res[index]) < indexw:
                res[index].append(" ")

            res[index] += letter

    return "\n".join(["".join(word) for word in res])
