def rectangles(strings: list):
    for s in strings:
        print(s)
    count = 0

    for line in range(len(strings) - 1):
        for col in range(len(strings[line]) - 1):
            for end_line in range(line + 1, len(strings)):
                for end_col in range(col + 1, len(strings[end_line])):
                    s1 = strings[line][col : end_col + 1]
                    #  print(f"s1: {list(s1)}")
                    s2 = "".join(
                        [l[end_col] for l in strings[line:]][line : end_line + 1]
                    )
                    #  print(f"s2: {list(s2)}")
                    s3 = strings[end_line][col : end_col + 1]
                    # print(f"s3: {list(s3)}")
                    s4 = "".join([l[col] for l in strings[line:]][line : end_line + 1])
                    # print(f"s4: {list(s4)}")

                    currentRect = [s1, s2, s3, s4]
                    # print(f"currentRect\n {currentRect}")
                    if validRectangle(currentRect):
                        count += 1
    return count


def validRectangle(sides):
    valid, direction = True, "-"

    for side in sides:
        if side == "":
            valid = False
        elif not validSide(side, direction):
            valid = False

        direction = "|" if direction == "-" else "-"

    return valid


def validSide(side, direction):
    valid, dirNotAllowed = True, "-" if direction == "|" else "|"

    if side[0] != "+" or side[-1] != "+":
        valid = False
    elif side.count(dirNotAllowed) > 0:
        valid = False
    elif side.count(" ") > 0:
        valid = False

    return valid
