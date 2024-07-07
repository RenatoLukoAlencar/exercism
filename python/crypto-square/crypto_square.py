def cipher_text(plain_text):
    norm = "".join(
        [l.lower() if l.isalnum() else "" for l in plain_text.replace(" ", "")]
    )

    column, row = 1, 1
    for c in range(len(norm)):
        for r in range(len(norm)):
            if c * r >= len(norm) and c >= r and c - r <= 1:
                row, column = r, c

            if (column, row) != 1 and row != 1:
                break

    norm += " " * ((column * row) - len(norm))
    splited = [norm[r : r + column] for r in range(0, len(norm), column)]
    inverted = ["" for _ in range(row + (1 if row != column else 0))]

    for r in range(row):
        for c in range(column):
            inverted[c] += splited[r][c]

    return " ".join(inverted) if inverted[0] != " " else ""
