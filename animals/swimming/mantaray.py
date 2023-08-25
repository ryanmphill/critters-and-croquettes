from animals.animal import Animal


class MantaRay(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num) # Set values via Animal class
        self.swimming = True

    def feed(self):
        print(f'{self.name} had the staff throw a belly dancing party so it would eat its {self.food}')