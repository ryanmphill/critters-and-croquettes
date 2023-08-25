from animals.animal import Animal

class Echidna(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num) # Set values via Animal class
        self.shift = shift
        self.walking = True
