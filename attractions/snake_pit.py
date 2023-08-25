class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "stupendous snakes of all sizes"
        self.animals = list()
    
    @property
    def last_critter_added(self):
        newest_critter = self.animals[-1]
        return f'{newest_critter.name} the {newest_critter.species} is the most recent addition to {self.attraction_name}'
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def add_animals(self, animal_list):
        for animal in animal_list:
            self.animals.append(animal)
    
    def report(self):
        animal_report = f"{self.attraction_name} is is where you'll find {self.description}, like\n"
        for animal in self.animals:
            animal_report += f"     * {animal.name} the {animal.species}\n"
        print(animal_report)
        return animal_report
