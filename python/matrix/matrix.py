class Matrix:
    def __init__(self, matrix_string):
        self.arr = []

        for index, row in enumerate(matrix_string.split("\n")):
            self.arr.append([])
            for n in row.split(" "):
                self.arr[index].append(int(n))

    def row(self, index):
        return self.arr[index - 1]

    def column(self, index):
        return [n[index - 1] for n in self.arr]
