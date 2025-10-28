class School:
    def __init__(self):
        pass
    def add_student(self, name, grade):
        students = {}
        self.students = students
        self.name = name 
        self.grade = grade
        students[name] = grade
        print(students)
        result = []
        result.append(name)
        return result
        

    def roster(self):
        pass

    def grade(self, grade_number):
        self.grade_number = grade_number

    def added(self):
            return True
        return False

school = School()
print(school.add_student('Aimee', 10))
print(school.added())