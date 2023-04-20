class Students:
    def GetInformation(self):
        print("student Lastname name is " + self.Lastname)
        print("student Firstname name is " + self.Firstname)
        print("student Adress name is " + self.Adress)
        print("student City name is " + self.City)
        print("student State name is " + self.State)
        print("student zipcode name is " + self.Zipcode)


student1 = Students()
student1.Lastname  = "Doe"
student1.Firstname = "Jane"
student1.Adress = "111 st"
student1.City = "Santa Ana"
student1.State = "CA"
student1.Zipcode = "12345\n"

student2 = Students()
student2.Lastname  = "Cantor"
student2.Firstname = "Mike"
student2.Adress = "222 st"
student2.City = "Garden Grove"
student2.State = "CA"
student2.Zipcode = "67890"

student3 = Students()
student3.Lastname  = input("Enter student's last name: ")
student3.Firstname = input("Enter student's first name:  ")
student3.Adress = input("Enter student's address: ")
student3.City = input("Enter student's city: ")
student3.State = input("Enter student's state: ")
student3.Zipcode = input("Enter student's zipcode: ")

student3.GetInformation()