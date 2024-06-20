class Garden:

    _dic = {"V": "Violets", "G": "Grass", "R": "Radishes", "C": "Clover"}

    def __init__(
        self,
        diagram,
        students=(
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Fred",
            "Ginny",
            "Harriet",
            "Ileana",
            "Joseph",
            "Kincaid",
            "Larry",
        ),
    ):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student)

        return [
            self._dic[self.diagram[0][index * 2]],
            self._dic[self.diagram[0][(index * 2) + 1]],
            self._dic[self.diagram[1][index * 2]],
            self._dic[self.diagram[1][(index * 2) + 1]],
        ]
