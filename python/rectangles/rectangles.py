def rectangles(strings: list):
    nL, count = [list(s) for s in strings], 0

    for row, line in enumerate(nL):
        for column, vertice in enumerate(line):
            for nextPoint in range(column + 1, len(line)):
                if vertice == "+" and line[nextPoint] == "+":
                    topSeg = line[column : nextPoint + 1]

                    if topSeg.count(" ") == 0:
                        allSeg = [topSeg]
                        for i in range(row, len(nL)):
                            if nL[i][column] == " " or nL[i][nextPoint] == " ":
                                break

                            seg = nL[i][column : nextPoint + 1]
                            allSeg.append(seg)

                            if (
                                seg[0] == "+"
                                and seg[-1] == "+"
                                and (seg.count(" ") == 0 and seg.count("|") == 0)
                            ):
                                count += 1

                        for x in allSeg:
                            print(f"xx: {x}")
    return count
