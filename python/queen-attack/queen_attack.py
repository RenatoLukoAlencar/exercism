class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        elif row > 7:
            raise ValueError("row not on board")
        elif column < 0:
            raise ValueError("column not positive")
        elif column > 7:
            raise ValueError("column not on board")

        self.row = row

        self.column = column

    def can_attack(self, another_queen):
        res, rows, columns = (
            False,
            self.row == another_queen.row,
            self.column == another_queen.column,
        )
        if rows and columns:
            raise ValueError("Invalid queen position: both queens in the same square")
        elif rows or columns:
            res = True
        else:
            difrow = abs(self.row - another_queen.row)
            difcol = abs(self.column - another_queen.column)
            res = difcol == difrow

        return res
