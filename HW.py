def mean(numbers):
    if numbers:
        if isinstance(numbers, dict):
            res=[]
            for value in numbers.values():
                res += value
            return sum(res)/len(res)
        else:
            return sum(numbers)/len(numbers)
    else:
        return 0
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
    def __str__(self):
        info = str(f"Имя: {self.name}\n"
                   f"Фамилия: {self.surname}\n"
                   f"Средняя оценка: {mean(self.grades)}\n"
                   f"Курсы в процессе обучения: {', '.join(self.courses_in_progress)}\n"
                   f"Завершенные курсы: {', '.join(self.finished_courses)}\n")
        return info
    def __lt__(self, other):
        return mean(self.grades) < mean(other.grades)
    def __gt__(self, other):
        return mean(self.grades) > mean(other.grades)
    def __le__(self, other):
        return mean(self.grades) <= mean(other.grades)
    def __ge__(self, other):
        return mean(self.grades) >= mean(other.grades)
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {mean(self.grades)}"
    def __lt__(self, other):
        return mean(self.grades) < mean(other.grades)
    def __gt__(self, other):
        return mean(self.grades) > mean(other.grades)
    def __le__(self, other):
        return mean(self.grades) <= mean(other.grades)
    def __ge__(self, other):
        return mean(self.grades) >= mean(other.grades)

class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

Student_1 = Student('Ruoy', 'Eman', 'your_gender')
Student_1.courses_in_progress += ['Python']
Student_1.courses_in_progress += ['Git']
Student_1.finished_courses += ['Introduction to the programming']

Student_2 = Student('Ron', 'Wuizli', 'your_gender')
Student_2.courses_in_progress += ['Python']
Student_2.finished_courses += ['Paint']
Student_2.finished_courses += ['Calculator']

Lecturer_1 = Lecturer('Leps', 'Grisha')
Lecturer_1.courses_attached += ['Python']
Lecturer_1.courses_attached += ['Java']

Lecturer_2 = Lecturer('Jigurda', 'Nikita')
Lecturer_2.courses_attached += ['JS']

Reviewer_1 = Reviewer('Nikolaev', 'Igor')
Reviewer_1.courses_attached += ['Python']
Reviewer_1.courses_attached += ['Git']

Reviewer_1.rate_hw(Student_1, 'Python', 8)
Reviewer_1.rate_hw(Student_1, 'Python', 9)
Reviewer_1.rate_hw(Student_1, 'Git', 10)
Reviewer_1.rate_hw(Student_2, 'Python', 10)
Reviewer_1.rate_hw(Student_2, 'Python', 6)

Student_1.rate_lecturer(Lecturer_1, 10)
Student_1.rate_lecturer(Lecturer_1, 9)
Student_2.rate_lecturer(Lecturer_1, 9)
Student_1.rate_lecturer(Lecturer_2, 7)

print(f"Reviewer_1:\n{Reviewer_1}\n")
print(f"Lecturer_1:\n{Lecturer_1}\n")
print(f"Lecturer_2:\n{Lecturer_2}\n")
print(f"Student_1:\n{Student_1}\n")
print(f"Student_2:\n{Student_2}\n")

print("Lecturer_1 < Lecturer_2 ==>", Lecturer_1 > Lecturer_2)
print("Student_1 > Student_2 ==>", Student_1 > Student_2)
