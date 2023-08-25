from datetime import date

class Animal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_num = chip_num # setting privately scoped __chip_num to make property read-only
        self.date_added = date.today()
    
    @property # Getter
    def chip_num(self):
        return self.__chip_num # now self.chip_num will actually return the private value. There is no actual chip_num attribute. So sneaky of us.
    
    @chip_num.setter # The setter
    def chip_num(self, num):
        pass # Tell the setter to do nothing, preventing __chip_num from being overwritten

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')