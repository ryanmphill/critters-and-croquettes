# import the python datetime module to help us create a timestamp
from datetime import date
from animals import (Llama, Goat, Echidna, Donkey, Alpaca)
from animals import (Anaconda, Copperhead, CornSnake, KingSnake, RatSnake)
from animals import (AngelFish, ClownFish, Eel, MantaRay, Salamander)
from animals import (Goose)
from attractions import (PettingZoo, Wetlands, SnakePit)

# self.swimming = True - These animals are in the tank
# self.slithering = True - These animals are in the pond
# self.walking = True - These animals are in the petting area
varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
slither_inn = SnakePit("Slither Inn", "stupendous snakes of all sizes")
blue_cave_cove = Wetlands("Blue Cave Cove", "aquatic critters of all kinds")


miss_fuzz = Llama("Miss Fuzz", "domestic llama", "midday", "oats", 1111111)
alpi = Alpaca("Alpi", "Eastern Alpaca", "morning", "straw", 1111112)
# print(miss_fuzz)
# miss_fuzz.feed()

mr_worm = KingSnake("Mr. Worm", "common kingsnake", "mice", 5555555)
copper = Copperhead("Copper", "Eastern Copperhead", "eggs", 9999999)
# print(mr_worm)
# mr_worm.feed()

miss_gills = ClownFish("Mrs. Gills", "common clownfish", "kelp", 2222222)
mr_manta = MantaRay("Mr. Manta", "southern mantaray", "plankton", 2222221)

varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(alpi)
varmint_village.report()

slither_inn.add_animal(mr_worm)
slither_inn.add_animal(copper)
slither_inn.report()

blue_cave_cove.add_animal(miss_gills)
blue_cave_cove.add_animal(mr_manta)
blue_cave_cove.report()

print("1st chip num",mr_worm.chip_num)
mr_worm.chip_num = 123456
print("2nd chip num",mr_worm.chip_num)

print(slither_inn.last_critter_added)
print(varmint_village.last_critter_added)
print(blue_cave_cove.last_critter_added)

miss_fuzz.feed()
mr_worm.feed()
mr_manta.feed()
miss_gills.feed()

bob = Goose("Bob", "Canada goose", "watercress sandwiches", 135791)
bob.run()
bob.swim()
varmint_village.add_animal(bob)
varmint_village.report()

print("*-----------------------------------------------------------------*")

dolly = Llama("Dolly", "miniature llama", "morning", "hay", 1033)
snappy = Eel("Snappy", "Moray Eel", "fish", 1044)
corny = CornSnake("Corny", "Eastern Cornsnake", "eggs", 999922)

varmint_village.add_animal(dolly)
slither_inn.add_animal(corny)
blue_cave_cove.add_animal(snappy)
slither_inn.add_animal(dolly)
blue_cave_cove.add_animal(dolly)
varmint_village.add_animal(snappy)