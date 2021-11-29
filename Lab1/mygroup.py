groupmates = [
    {
        "name": "Сергей",
        "surname": "Иванов",
        "exams": ["Информатика", "МЛиТА", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]


def print_students():
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in groupmates:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))


print_students()


def count_mark(groupmates):
    print(u"Имя".ljust(15), u"Фамилия".ljust(8), u"Экзамены".ljust(8), u"Оценки".ljust(20))
    for student in groupmates:
        marks_list = student['marks']
        result = (sum(marks_list) / len(marks_list))
        if result >= need:
            print(student["name"].ljust(15), student["surname"].ljust(8), str(student["exams"]).ljust(8),
                  str(student["marks"]).ljust(20))


need = int(input('Введите среднюю оценку :'))

count_mark(groupmates)
