class Class:
    __students_count = 22
    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > len(self.students):
            pass

    def get_average_grade(self):
        pass

    def __repr__(self):
        return f'The students in {self.name}: {self.students}. Average grade: {self.grades}'