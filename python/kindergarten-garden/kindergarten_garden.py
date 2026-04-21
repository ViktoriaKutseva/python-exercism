class Garden:
    def __init__(self, diagram, students: list | None = None) -> None:
        self.diagram = diagram.splitlines()     
        if students is None:
            students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
        self.students = sorted(students)
        self.plants_map = {
            'V': 'Violets',
            'R': 'Radishes',
            'C': 'Clover',
            'G': 'Grass'
        }

    def plants(self, student: str) -> list:
        index = self.students.index(student)
        correct_list_of_plants = []
        for row in self.diagram:
            plants_codes = row[index*2:index*2+2]
            for code in plants_codes:
                correct_list_of_plants.append(self.plants_map[code])
        return correct_list_of_plants
