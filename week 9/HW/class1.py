class Pet:
    def __init__(self, Name):
        self.Name = Name

    def set_Name(self, Name):
        self.Name = Name 

    def get_Name(self):
        return f"Pet name: {self.Name}"
def main(): 
    Name = str(input("Enter name "))
    p1 = Pet.set_Name = Name
    Pet.get_Name(p1)
main()

   