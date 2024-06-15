def saddle_points(matrix):
    if not all([len(elem) == len(matrix[0]) for elem in matrix]):
        raise ValueError("irregular matrix")

    res = []

    for i_row, row in enumerate(matrix):
        for i_col, col in enumerate(row):
            column = [elem[i_col] for elem in matrix]
            if all([col >= r for r in row]) and all([col <= c for c in column]):
                res.append({"row": i_row + 1, "column": i_col + 1})

    return res
