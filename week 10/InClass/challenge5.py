class Insect:

    def __init__(self, body, legs, antennae):
        self.__body = body
        self.__legs = legs
        self.__antennae = antennae


    def set_body(self, body):
        self.__body = body

    def set_legs(self, legs):
        self.__legs = legs

    def set_antennae(self, antennae):
        self.__antennae = antennae

    def get_body(self):
        return self.__body
    
    def get_legs(self):
        return self.__legs

    def get_antennae(self):
        return self.__antennae
    
class Bumblebee(Insect):

    def __init__(self, body, legs, antennae, characteristic):
        Insect.__init__(self, body, legs, antennae)
        
        self.__characteristic = characteristic

    def set_characteristic(self, characteristic):
        self.__characteristic = characteristic

    def get_characteristic(self):
        return self.__characteristic
    
class Grasshopper(Insect):
    
    def __init__(self, body, legs, antennae, characteristic):
        Insect.__init__(self, body, legs, antennae)
        
        self.__characteristic = characteristic

    def set_characteristic(self, characteristic):
        self.__characteristic = characteristic

    def get_characteristic(self):
        return self.__characteristic
    
def main():

    bumblebee = Bumblebee("3 body parts","3 pairs of jointed leg","1 pair of antenna","")
    print(f'Bumblebee has {bumblebee.get_body()}.')
    print(f'Bumblebee has {bumblebee.get_legs()}.')
    print(f'Bumblebee has {bumblebee.get_antennae()}.')
    bumblebee.set_characteristic("the ability to sting")
    print(f'Bumblebee has {bumblebee.get_characteristic()}.\n')

    grasshopper = Grasshopper("3 body parts","3 pairs of jointed leg","1 pair of antenna","")
    print(f"Grass hopper has {grasshopper.get_body()}.")
    print(f"Grass hopper has {grasshopper.get_legs()}.")
    print(f"Grass hopper has {grasshopper.get_antennae()}.")
    grasshopper.set_characteristic("the ability to jump")
    print(f"Grass hopper has {grasshopper.get_characteristic()}.\n")


main()