from student.student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, age):
        student = Student(name, age)
        self.students.append(student)

    def list_students(self):
        if not self.students:
            print("O'quvchilar ro'yxati bo'sh")
        else:
            print("O'quvchilar ro'yxati:")
            for idx, student in enumerate(self.students, start=1):
                print(f"{idx}. {student}")

    def remove_student(self, index):
        if 0 <= index < len(self.students):
            removed = self.students.pop(index)
            print(f"{removed.name} o'chirildi!")
        else:
            print("Noto'g'ri raqam!")
