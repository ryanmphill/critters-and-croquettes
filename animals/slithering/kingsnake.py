from animals.animal import Animal

class KingSnake(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num) # Set values via Animal class
        self.slithering = True

    def feed(self):
        print(f'{self.name} had its {self.food} flash frozen, and then proceeded to eat')
