class person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(person):
    def __init__(self, name, age, studentID, GPA):

        name = input('Enter the student name: ')
        age = input('Enter the student age: ')
        studentID = input('Enter the Student ID: ')
        GPA = input('Enter the student GPA: ')

        super().__init__(name, age)

        self.studentID = studentID
        self.GPA = GPA

class Teacher(person):
    def __init__(self, name, age, TeacherID, ClassTeaching):
        super().__init__(name, age)

        name = input('Enter the teacher name: ')
        age = input('Enter the teacher age: ')
        TeacherID = input('Enter the Teacher ID: ')
        ClassTeaching = input('Enter the name of the course teaching: ')

        self.TeacherID = TeacherID
        self.ClassTeaching = ClassTeaching

student = Student('Jane Doe', 25, 777, 3.8)
print("Student Name: ", student.name)
print("Student Age: ", student.age)
print("Student ID: ", student.studentID)
print("Student GPA: ", student.GPA)

print("\n")

teacher = Teacher("Ms.Cantor", 45, 7, "Python")
print("Teacher Name: ", teacher.name)
print("Teacher Age: ", teacher.age)
print("Teacher ID: ", teacher.TeacherID)
print("Teacher Course: ", teacher.ClassTeaching)