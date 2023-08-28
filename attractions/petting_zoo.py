from attractions.attraction import Attraction

class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    # 1: Duck typing check (pythonic)
    def add_animal(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal.name} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f'{animal.name} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')
    
    # Add multiple
    def add_animals(self, animals):
        for animal in animals:
            try:
                if animal.walk_speed > -1:
                    self.animals.append(animal)
                    print(f"{animal.name} now lives in {self.attraction_name}")
            except AttributeError as ex:
                print(f'{animal.name} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')
    