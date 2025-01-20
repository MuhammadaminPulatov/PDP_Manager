class Pupil:
    def __init__(self, name, familiya, yil, maktab):
        self.name = name
        self.familiya = familiya
        self.yil = yil
        self.maktab = maktab

    def info(self):
        return f"O'quvchi: {self.name} {self.familiya}, {self.yil}-yilda tug'ilgan, {self.maktab}-maktabda o'qiydi!"


class Student:
    def __init__(self, name, familiya, yil, kursi, fakultet):
        self.name = name
        self.familiya = familiya
        self.yil = yil
        self.kursi = kursi
        self.fakultet = fakultet

    def info(self):
        return f"Talaba: {self.name} {self.familiya}, {self.yil}-yilda tug'ilgan, {self.fakultet} fakulteti {self.kursi}-kurs talabasi!"


class PDPManager:
    def __init__(self):
        self.students = []
        self.pupils = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            return "Talaba muvaffaqqiyatli qo'shildi!"
        return "Xatolik: Student obyekti bo'lishi kerak!"

    def add_pupil(self, pupil):
        if isinstance(pupil, Pupil):
            self.pupils.append(pupil)
            return "O'quvchi muvaffaqiyatli qo'shildi!"
        return "Xatolik: Pupil obyekti bo'lishi kerak!"

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            return "Talaba o'chirildi!"
        return "Bunday talaba topilmadi!"

    def remove_pupil(self, pupil):
        if pupil in self.pupils:
            self.pupils.remove(pupil)
            return "O'quvchi o'chirildi!"
        return "Bunday o'quvchi topilmadi!"

    def get_all_students(self):
        return [student.info() for student in self.students]

    def get_all_pupils(self):
        return [pupil.info() for pupil in self.pupils]

