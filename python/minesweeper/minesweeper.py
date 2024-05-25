def annotate(minefield):
    if len(minefield) == 1:
        return [""]

    try:
        checkLenLines = []
        for line in minefield:
            checkLenLines.append(len(line))

        if not all(checkLenLines):
            raise Exception
        mx = len(minefield)
        my = len(minefield[0])
        board = [" " for _ in range(my) for _ in range(mx)]

        return board
    except:
        raise ValueError("The board is invalid with current input.")
