from animals.animal import Animal

class Anaconda(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num) # Set values via Animal class
        self.slithering = True
