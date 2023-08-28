from attractions.attraction import Attraction
from movements import Swimming

class Wetlands(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    # Number 2: Actual typing check (Common in C# and Java)
    def add_animal(self, animal):
        if isinstance(animal, Swimming):
            self.animals.append(animal)
            print(f"{animal.name} now lives in {self.attraction_name}")
        else:
            print(f'{animal.name} isn\'t a very good swimmer, so please do not try to put it in the {self.attraction_name} attraction.')
    
    # Add multiple
    def add_animals(self, animals):
        for animal in animals:
            if isinstance(animal, Swimming):
                self.animals.append(animal)
                print(f"{animal.name} now lives in {self.attraction_name}")
            else:
                print(f'{animal.name} isn\'t a very good swimmer, so please do not try to put it in the {self.attraction_name} attraction.')
