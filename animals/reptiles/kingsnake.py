from animals.animal import Animal
from movements import Slithering

class KingSnake(Animal, Slithering):

    def __init__(self, name, species, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def feed(self):
        print(f'{self.name} had its {self.food} flash frozen, and then proceeded to eat')
