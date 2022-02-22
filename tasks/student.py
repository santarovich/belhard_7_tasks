"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: int
    average_score: float

    def __init__(self, surname, name, group, average_score):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __le__(self, other):
        return self.average_score <= other.average_score

    def __str__(self):
        return f"{self.name} {self.surname}, group no. {self.group}, average score {self.average_score}"


# student_1 = Student("Hofstadter", "Leonard", 753159, 7.2)
# student_2 = Student("Cooper", "Sheldon", 8426, 9.7)
# student_3 = Student("Hofstadter", "Penny", 321632, 3.1)
# student_4 = Student("Wolowitz", "Howard", 96302, 6.4)
# student_5 = Student("Koothrappali", "Raj", 753159, 8.3)
# print(student_1)
# print(student_2)
# print(student_3)
# print(student_4)
# print(student_5)
