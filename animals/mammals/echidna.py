from animals.animal import Animal
from movements import Walking

class Echidna(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift
