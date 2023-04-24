class Pet:
    def __init__(self, name=None, animal_type = None, age = 0):
         self._name = name
         self._animal_type = animal_type
         self._age = age
      
    def get_name(self):
        return self._name
      
    def set_name(self, x):
        self._name = x

    def get_animal_type(self):
        return self._animal_type
      
    def set_animal_type(self, y):
        self._animal_type = y

    def get_age(self):
        return self._age
      
    def set_age(self, z):
        self._age = z

    def pet_attributes(self):
        print(f"\nYour pet's name is: {raj.get_name()}")
        print(f"Your pet's type is: {raj.get_animal_type()}")
        print(f"Your pet's age is: {raj.get_age()}")
  
raj = Pet()
  
name = input("Enter pet's name: ")
raj.set_name(name)

animal_type = input("Enter animal type: ")
raj.set_animal_type(animal_type)

age = input("Enter pet's age: ")
raj.set_age(age)

raj.pet_attributes()