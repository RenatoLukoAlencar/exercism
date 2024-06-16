class School:
    def __init__(self):
        self.classes = {}
        self.history = []

    def add_student(self, name, grade):
        if grade not in self.classes.keys():
            self.classes.setdefault(grade, [])

        for group in self.classes.values():
            for student in group:
                if student == name:
                    self.history.append(False)
                    return False

        self.classes[grade].append(name)
        self.history.append(True)
        return self.history[-1]

    def roster(self):
        res = []
        for i in sorted(self.classes.keys()):
            res += sorted(self.classes[i])

        return res

    def grade(self, grade_number):
        return (
            sorted(self.classes[grade_number])
            if grade_number in self.classes.keys()
            else []
        )

    def added(self):
        return self.history
