import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from student import Student
from teacher import Teacher

class Application:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("School Application")
        self.main_window.geometry("400x300")

        self.students = []
        self.teachers = []

        self.add_student_button = tk.Button(self.main_window, text="Add Student", command=self.add_student)
        self.add_student_button.pack(pady=10)

        self.add_teacher_button = tk.Button(self.main_window, text="Add Teacher", command=self.add_teacher)
        self.add_teacher_button.pack(pady=10)

        self.display_info_button = tk.Button(self.main_window, text="Display Info", command=self.display_info)
        self.display_info_button.pack(pady=10)

        self.quit_button = tk.Button(self.main_window, text="Quit", command=self.main_window.quit)
        self.quit_button.pack(pady=10)

    def run(self):
        self.main_window.mainloop()

    def add_student(self):
        student_name = self.ask_string_dialog("Add Student", "Enter student name:")
        student_age = self.ask_integer_dialog("Add Student", "Enter student age:")
        if student_name and student_age:
            student = Student(student_name, student_age)
            self.students.append(student)
            messagebox.showinfo("Success", "Student added successfully.")
        else:
            messagebox.showwarning("Error", "Invalid student name or age.")

    def add_teacher(self):
        teacher_name = self.ask_string_dialog("Add Teacher", "Enter teacher name:")
        teacher_subject = self.ask_string_dialog("Add Teacher", "Enter teacher subject:")
        if teacher_name and teacher_subject:
            teacher = Teacher(teacher_name, teacher_subject)
            self.teachers.append(teacher)
            messagebox.showinfo("Success", "Teacher added successfully.")
        else:
            messagebox.showwarning("Error", "Invalid teacher name or subject.")

    def display_info(self):
        info = ""
        if self.students:
            info += "Students:\n"
            for student in self.students:
                info += f"Name: {student.name}, Age: {student.age}\n"
            info += "\n"
        if self.teachers:
            info += "Teachers:\n"
            for teacher in self.teachers:
                info += f"Name: {teacher.name}, Subject: {teacher.subject}\n"
        if not self.students and not self.teachers:
            info = "No information available."
        messagebox.showinfo("Information", info)

    def ask_string_dialog(self, title, prompt):
        dialog_window = tk.Toplevel(self.main_window)

        prompt_label = tk.Label(dialog_window, text=prompt)
        prompt_label.pack(padx=10, pady=10)

        input_entry = tk.Entry(dialog_window)
        input_entry.pack(padx=10, pady=10)

        confirm_button = tk.Button(dialog_window, text="OK", command=lambda: self.get_dialog_input(dialog_window, input_entry))
        confirm_button.pack(padx=10, pady=10)

        dialog_window.title(title)
        dialog_window.geometry("300x150")
        dialog_window.transient(self.main_window)
        dialog_window.grab_set()
        self.main_window.wait_window(dialog_window)

        return self.dialog_input

    def ask_integer_dialog(self, title, prompt):
        dialog_window = tk.Toplevel(self.main_window)

        prompt_label = tk.Label(dialog_window, text=prompt)
        prompt_label.pack(padx=10, pady=10)

        input_entry = tk.Entry(dialog_window)
        input_entry.pack(padx=10, pady=10)

        confirm_button = tk.Button(dialog_window, text="OK", command=lambda: self.get_dialog_input(dialog_window, input_entry))
        confirm_button.pack(padx=10, pady=10)

        dialog_window.title(title)
        dialog_window.geometry("300x150")
        dialog_window.transient(self.main_window)
        dialog_window.grab_set()
        self.main_window.wait_window(dialog_window)

        return self.dialog_input

    def get_dialog_input(self, window, entry):
        self.dialog_input = entry.get()
        window.destroy()

