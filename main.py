
class Student:



    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.me_course = []




    def ever_grade(self):
        suma = sum(map(sum, self.grades.values()))
        kol = sum(len(x) for x in self.grades.values())
        re = suma // kol

        return re


    def kek(self):
        res = ",".join(self.courses_in_progress)
        return res

    def kek_2(self):
        res = ",".join(self.finished_courses)
        return res

    def __str__(self):
        res = f" Имя: {self.name} \n" \
              f" Фамилия: {self.surname} \n" \
              f" Средняя оценка за ДЗ: { self.ever_grade() } \n" \
              f" Курсы в процессе изучения: {self.kek()} \n" \
              f" Завершенные курсы: {self.kek_2()}"
        return res

    def teacher_evaluation(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.teaches and course in self.me_course:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f"{other.name} Не студент")
        elif self.ever_grade() > other.ever_grade():
            return (f"Успеваемость студента {self.name}  {self.surname}  выше")
        else:
            return(f"Успеваемость студента {other.name} {other.surname} выше")





class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f" Имя: {self.name}, \n" \
              f" Фамилия: {self.surname}"
        return res

class Lecturer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.teaches = []


    def average_rating(self):
        suma = sum(map(sum, self.grades.values()))
        kol = sum(len(x) for x in self.grades.values())
        res = suma // kol
        return (f"Средняя оценка {self.name} за лекцию:{res}")

    def __str__(self):
        res = f" Имя: {self.name} \n" \
              f" Фамилия: {self.surname} \n" \
              f"  {self.average_rating()}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f"{other.name} Не Лектор")
        elif self.average_rating() > other.average_rating():
            return(f"Лектор {self.name} нравится студентам больше")
        else:
            return(f"Лектор {other.name} нравится студентам больше")


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



    def __str__(self):
        res = f" Имя: {self.name} \n" \
              f" Фамилия: {self.surname}"
        return res

#Хороший ученик
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.me_course += ['Python']
best_student.finished_courses += ["Введение в программирование"]

#Плохой ученик
bad_student = Student('Mark', 'man', 'your_gender')
bad_student.courses_in_progress += ['Python', 'Git']
bad_student.me_course += ['Python']
bad_student.finished_courses += ["Введение в программирование"]

#Ревьюеры сыны ментора
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(bad_student, 'Python', 4)
cool_reviewer.rate_hw(bad_student, 'Python', 3)
cool_reviewer.rate_hw(bad_student, 'Python', 4)
norm_reviewer = Reviewer('Игорь', 'Тело')
norm_reviewer.courses_attached += ['Python']
norm_reviewer.courses_attached += ['Git']
norm_reviewer.rate_hw(best_student, 'Python', 10)
norm_reviewer.rate_hw(best_student, 'Python', 10)
norm_reviewer.rate_hw(best_student, 'Python', 10)
norm_reviewer.rate_hw(bad_student, 'Python', 4)
norm_reviewer.rate_hw(bad_student, 'Python', 3)
norm_reviewer.rate_hw(bad_student, 'Python', 4)

#Jwtyrb 2
norm_reviewer.rate_hw(best_student, 'Git', 6)
norm_reviewer.rate_hw(best_student, 'Git', 9)
norm_reviewer.rate_hw(best_student, 'Git', 10)
norm_reviewer.rate_hw(bad_student, 'Git', 7)
norm_reviewer.rate_hw(bad_student, 'Git', 6)
norm_reviewer.rate_hw(bad_student, 'Git', 5)

#Плохой учитель
not_bad_lecturer = Lecturer("Juan", "Bishop")
not_bad_lecturer.teaches = ["Python"]
#Хороший учитель
cool_lecturer = Lecturer("Helen ", "Huff")
cool_lecturer.teaches = ["Python"]
#Плохой студент
bad_student.teacher_evaluation(not_bad_lecturer, 'Python', 2)
bad_student.teacher_evaluation(cool_lecturer, 'Python', 10)
bad_student.teacher_evaluation(not_bad_lecturer, 'Python', 2)
bad_student.teacher_evaluation(cool_lecturer, 'Python', 10)
#Хороший студент
best_student.teacher_evaluation(not_bad_lecturer, 'Python', 8)
best_student.teacher_evaluation(cool_lecturer, 'Python', 10)
best_student.teacher_evaluation(not_bad_lecturer, 'Python', 8)
best_student.teacher_evaluation(cool_lecturer, 'Python', 10)


print(cool_reviewer)
print(norm_reviewer)
print(not_bad_lecturer)
print(cool_lecturer)
print(best_student)
print(bad_student)
print(best_student.ever_grade())
print(not_bad_lecturer.grades)
print(bad_student.grades)
print(cool_lecturer.__lt__(not_bad_lecturer))
print(bad_student.__lt__(best_student))
print(cool_lecturer.average_rating())


######ЗАДАНИЕ 4
s = [best_student, bad_student ]
l = [not_bad_lecturer, cool_lecturer]

def general_assessment_student(spisok, cou):
    s = []
    for stu in spisok:
        for key, val in stu.grades.items():
            if cou == key:
               for v in val:
                   s.append(v)
    i = sum(s)
    m = len(s)
    res = i // m
    print(f"Средняя оценка студентов по предмету {cou}: {res}"  )




def general_assessment_lecturer(spisok, cou):
    s = []
    for stu in spisok:
        for key, val in stu.grades.items():
            if cou == key:
               for v in val:
                   s.append(v)
    i = sum(s)
    m = len(s)
    res = i//m
    print(f"Средняя оценка лекторов по предмету {cou}: {res}" )


general_assessment_student(s, 'Python')
general_assessment_lecturer(l, 'Python')





