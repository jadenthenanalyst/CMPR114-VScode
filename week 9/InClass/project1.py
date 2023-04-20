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

student1.GetInformation()
student2.GetInformation()