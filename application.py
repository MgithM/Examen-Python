import colorama
from colorama import Fore
from student import Student
from teacher import Teacher

class Application:
    def __init__(self):
        self.university = "Open University"
        self.students = []
        self.teachers = []

    def launch(self):
        self.print_welcome_message()
        self.create_students()
        self.create_teachers()
        self.display_students()
        self.display_teachers()

    def print_welcome_message(self):
        print(Fore.GREEN + "Welcome to our Python application!")
        print("University: ", self.university)

    def create_students(self):
        print(Fore.YELLOW + "\n=== Create Students ===")
        for i in range(5):
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            student = Student(name, age)
            self.students.append(student)

    def create_teachers(self):
        print(Fore.YELLOW + "\n=== Create Teachers ===")
        for i in range(5):
            name = input("Enter teacher name: ")
            subject = input("Enter teacher subject: ")
            teacher = Teacher(name, subject)
            self.teachers.append(teacher)

    def display_students(self):
        print(Fore.CYAN + "\n=== Students ===")
        for student in self.students:
            student.display_info()

    def display_teachers(self):
        print(Fore.CYAN + "\n=== Teachers ===")
        for teacher in self.teachers:
            teacher.display_info()
