class person:

    def __init__(self,name,age, address, city, state, zipcode):

        self.name = name
        self.age = age
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

class Student(person):
    def __init__(self, name,age, address, city, state, zipcode, studentID, GPA):

        super().__init__(name,age, address, city, state, zipcode)

        studentID = input('Enter the Student ID: ')
        GPA = input('Enter the student GPA: ')

        self.studentID = studentID
        self.GPA = GPA

class Teacher(person):
    def __init__(self, name,age, address, city, state, zipcode, TeacherID, ClassTeaching):

        super().__init__(name,age, address, city, state, zipcode)
        
        TeacherID = input('Enter the Teacher ID: ')
        ClassTeaching = input('Enter the name of the course teaching: ')
        self.TeacherID = TeacherID
        self.ClassTeaching = ClassTeaching

student = Student("Jaden Tran", 31, "2406 Mark St", "Santa Ana", "CA", 92703, 12345, 4.0)
print("Student Name: ", student.name)
print("Student Age: ", student.age)
print("Student Adress: ", student.address)
print("Student State: ", student.state)
print("Student City: ", student.city)
print("Student Zipcode: ", student.zipcode)
print("Student ID: ", student.studentID)
print("Student GPA: ", student.GPA)

print("\n")

teacher = Teacher("Dan Huynh", 50, "1234 Bolsa Ave", "Westminster", "CA", 92683, 6789, "Python")
print("Teacher Name: ", teacher.name)
print("Teacher Age: ", teacher.age)
print("Teacher Adress: ", teacher.address)
print("Teacher City: ", teacher.city)
print("Teacher State: ", teacher.state)
print("Teacher Zipcode: ", teacher.zipcode)
print("Teacher ID: ", teacher.TeacherID)
print("Teacher Course: ", teacher.ClassTeaching)
