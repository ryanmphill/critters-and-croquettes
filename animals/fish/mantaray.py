from animals.animal import Animal
from movements import Swimming

class MantaRay(Animal, Swimming):

    def __init__(self, name, species, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)

    def feed(self):
        print(f'{self.name} had the staff throw a belly dancing party so it would eat its {self.food}')