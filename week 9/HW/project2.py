class Employee:
    def __init__(self, Name, ID_Number, Department, Job_Title):
        self.Name = Name
        self.ID_Number = ID_Number
        self.Department = Department
        self.Job_Title = Job_Title

    def GetEmployee(self):
        print("Employee name is: " + self.Name)
        print("Employee ID Number is: " + str(self.ID_Number))
        print("Employee Department is: " + self.Department)
        print("Employee Job Title is: " + self.Job_Title + "\n")

emp1 = Employee("Susan Meyers",47899,"Accounting","Vice President")
emp2 = Employee("Mark Jones",39119,"IT","Programmer")
emp3 = Employee("Joy Rogers",81774,"Manufacturing","Engineer")
emp1.GetEmployee()
emp2.GetEmployee()
emp3.GetEmployee()
