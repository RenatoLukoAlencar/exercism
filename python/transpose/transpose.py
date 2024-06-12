def transpose(lines):
    print(f"lines: {lines}")
    res = []

    for index, item in enumerate(lines):
        print(f"i: {index}, item: {item}")

        if len(res) - 1 < index:
            res.append([])

        res[index].append(item)

    for index, line in enumerate(res):
        res[index] = "".join(line)

    print(f"res: {res}")

    return res
