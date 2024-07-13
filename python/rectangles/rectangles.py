def rectangles(strings: list):
    newList, count = [], 0
    for s in strings:
        newList.append(list(s))

    for l, line in enumerate(newList):
        if l != len(newList) - 1:
            twoOrMore = line.count("+") >= 2

            if twoOrMore:
                # print(f"line{l +1}: {line}")
                # print(f"    this line contain {line.count("+")}")
                lineIndexs = []
                for c, col in enumerate(line):
                    if col == "+":
                        lineIndexs.append(c)

                for startCorner in range(len(lineIndexs)):
                    if startCorner != len(lineIndexs) - 1:
                        segment = line[
                            lineIndexs[startCorner] : lineIndexs[startCorner + 1] + 1
                        ]
                        if segment.count(" ") == 0:
                            # print(f"      segment{startCorner}: {segment}")

                            allseg = [str(segment)]
                            seqRow = l + 1
                            while l + seqRow <= len(newList) - 2:

                                if (
                                    newList[seqRow][0] == " "
                                    or newList[seqRow][-1] == " "
                                ):
                                    break

                                seqRow += 1

                            count += 1
    return count
