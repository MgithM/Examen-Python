import colorama
from colorama import Fore

class Teacher:
    university = "Open University"

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_info(self):
        print(Fore.YELLOW + "Name:", self.name)
        print("Subject:", self.subject)
        print("University:", self.university)
        print("Courses:", self.courses)
        print()
