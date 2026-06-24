class Student:
    total_students = 0

    def __init__(self, roll_no, marks, grade):
        self.__roll_no = roll_no
        self.__marks = marks
        self._grade = grade
        Student.total_students += 1

    @property
    def gpa(self):
        return sum(self.__marks) / len(self.__marks) / 10

    @gpa.setter
    def gpa(self, marks):
        for m in marks:
            if m < 0 or m > 100:
                raise ValueError("Marks must be between 0 and 100")
        self.__marks = marks

    @classmethod
    def count(cls):
        return cls.total_students


# Example
s1 = Student(101, [80, 90, 85], "A")
s2 = Student(102, [70, 75, 80], "B")

print("GPA:", s1.gpa)

s1.gpa = [90, 95, 88]
print("New GPA:", s1.gpa)

print("Total Students:", Student.count())