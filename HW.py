class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, grade):
        if isinstance(lecturer, Lecturer) and (set(self.courses_in_progress) & set(lecturer.courses_attached)):
            if isinstance(grade, int) and (0 <= grade <= 10) :
                lecturer.grades += [grade]
            else:
                print("Оценка введена неверно")
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

Lecturer_1 = Lecturer('Leps', 'Grisha')
Lecturer_1.courses_attached += ['Python']
Lecturer_1.courses_attached += ['Java']

Lecturer_2 = Lecturer('Jigurda', 'Nikita')
Lecturer_2.courses_attached += ['JS']

Reviewer_1 = Reviewer('Nikolaev', 'Igor')
Reviewer_1.courses_attached += ['Python']

Reviewer_1.rate_hw(best_student, 'Python', 8)
Reviewer_1.rate_hw(best_student, 'Python', 9)
Reviewer_1.rate_hw(best_student, 'Python', 10)

best_student.rate_lecturer(Lecturer_1, 10)
best_student.rate_lecturer(Lecturer_1, 9)
best_student.rate_lecturer(Lecturer_2, 7)
print("student:", best_student.grades)
#print("rev1:", Reviewer_1.__dict__)
print("lec1:", Lecturer_1.grades)
print("lec2:", Lecturer_2.grades)
