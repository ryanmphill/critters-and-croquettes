from datetime import date
from animals.animal import Animal

class Llama(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num) # Set values via Animal class
        self.shift = shift
        self.walking = True

    def feed(self):
        print(f'On {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')