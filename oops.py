#BLUEPRINT
class Student:

    def __init__(self, name, age, marks):
        self.name = name # obj attr.     [obj attr. > class attr.]
        self.age = age
        self.marks = marks

    def get_name(self):
        print(self.name)

    def get_marks(self):
        print(self.marks)

# instance
s_1 = Student("harman", 20, 99)
s_2 = Student("karan", 2, 78)
s_1.get_name()
s_2.get_marks()
