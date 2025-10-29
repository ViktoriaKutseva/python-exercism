class School:
    def __init__(self):
        self.roster_list = []
        self.success = []
        
    def add_student(self, name, grade):
        names = [name_student for name_student, _ in self.roster_list]
        if (name) not in names:
            self.roster_list.append((name, grade))
            self.success.append(True)
        else:
            self.success.append(False)
        
    def roster(self):
        students = []
        student_names = []
        if self.roster_list:
            for student in self.roster_list:
                students.append(student)
        students.sort(key=lambda t: (t[1], t[0]))
        for name in students:
            student_names.append(name[0])
            
        return student_names           

    def grade(self, grade_number):
        students = []
        for student in self.roster_list:
            if grade_number == student[1]:
                students.append(student)
            else:
                continue
        students.sort(key=lambda t: (t[1], t[0]))
        names = [name_student for name_student, _ in students]
        return names 
    
    def added(self):
        return self.success
