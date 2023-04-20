class PI:

    def GetInformation(self, LN, FN, Age, Adress, City, State, Zipcode):
        return LN + " , " + FN + " , " + str(Age) + " , " + Adress+ " , " + City + " , " + State + " , " +str(Zipcode)
    
PersonalInformation = PI()
PersonalInformation.Lastname = input("Enter the lastname: ")
PersonalInformation.Firstname = input("Enter the first name: ")
PersonalInformation.Age = int(input("Enter the age: "))
PersonalInformation.Adress = input("Enter the adress: ")
PersonalInformation.City = input("Enter the city: ")
PersonalInformation.State = input("Enter the state: ")
PersonalInformation.Zipcode = int(input("Enter the zipcode: "))

print(PersonalInformation.GetInformation(PersonalInformation.Lastname, PersonalInformation.Firstname, PersonalInformation.Age,
        PersonalInformation.Adress,PersonalInformation.City,PersonalInformation.State, PersonalInformation.Zipcode ))