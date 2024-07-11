def rectangles(strings: list):
    newList, count = [], 0
    for s in strings:
        newList.append(list(s))

    for l, line in enumerate(newList):
        for r, row in enumerate(line):
            if newList[l][r] == "+":
                count += 1

    return count
