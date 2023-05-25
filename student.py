import colorama
from colorama import Fore

class Student:
    university = "Open University"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    def display_info(self):
        print(Fore.YELLOW + "Name:", self.name)
        print("Age:", self.age)
        print("University:", self.university)
        print("Grades:", self.grades)
        print("Average Grade:", self.get_average_grade())
        print()
