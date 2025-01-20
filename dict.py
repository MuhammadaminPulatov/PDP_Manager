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
        self.students = {}
        self.pupils = {}

    def add_student(self, student):
        if isinstance(student, Student):
            key = f"{student.name}_{student.familiya}"
            self.students[key] = student
            return "Talaba muvaffaqqiyatli qo'shildi!"
        return "Xatolik: Student obyekti bo'lishi kerak!"

    def add_pupil(self, pupil):
        if isinstance(pupil, Pupil):
            key = f"{pupil.name}_{pupil.familiya}"
            self.pupils[key] = pupil
            return "O'quvchi muvaffaqiyatli qo'shildi!"
        return "Xatolik: Pupil obyekti bo'lishi kerak!"

    def remove_student(self, student):
        key = f"{student.name}_{student.familiya}"
        if key in self.students:
            del self.students[key]
            return "Talaba o'chirildi!"
        return "Bunday talaba topilmadi!"

    def remove_pupil(self, pupil):
        key = f"{pupil.name}_{pupil.familiya}"
        if key in self.pupils:
            del self.pupils[key]
            return "O'quvchi o'chirildi!"
        return "Bunday o'quvchi topilmadi!"

    def get_all_students(self):
        return [student.info() for student in self.students.values()]

    def get_all_pupils(self):
        return [pupil.info() for pupil in self.pupils.values()]

    manager = PDPManager()

    pupil1 = Pupil("Ali", "Saidov", 2005, "123")
    student1 = Student("Vali", "Rahimov", 2003, 2, "Informatika")

    print(manager.add_pupil(pupil1))
    print(manager.add_student(student1))

    print("Barcha talabalar:")
    print(manager.get_all_students())

    print("Barcha o'quvchilar:")
    print(manager.get_all_pupils())

    print(manager.remove_student(student1))
    print(manager.remove_pupil(pupil1))

    print("O'chirishdan keyin barcha talabalar:")
    print(manager.get_all_students())

    print("O'chirishdan keyin barcha o'quvchilar:")
    print(manager.get_all_pupils())