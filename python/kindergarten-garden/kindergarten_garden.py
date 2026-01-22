class Garden:
    def __init__(self, diagram, students):
        self.diagram = diagram.splitlines()
        students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
        self.students = sorted(students)

    def plants(self) -> list:
        return self.diagram