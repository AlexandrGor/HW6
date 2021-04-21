class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    pass
class Reviewer(Mentor):
    pass

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

Lecturer_1 = Lecturer('Leps', 'Grisha')
Lecturer_1.courses_attached += ['Python']
Lecturer_1.courses_attached += ['Java']
Reviewer_1 = Reviewer('Nikolaev', 'Igor')
Reviewer_1.courses_attached += ['Python']


Reviewer_1.rate_hw(best_student, 'Python', 10)
Reviewer_1.rate_hw(best_student, 'Python', 10)
Lecturer_1.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
print(Reviewer_1.__dict__)
