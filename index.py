# import the python datetime module to help us create a timestamp
from datetime import date
from walking import (Llama, Goat, Echidna, Donkey, Alpaca)
from slithering import (Anaconda, Copperhead, CornSnake, KingSnake, RatSnake)
from swimming import (AngelFish, ClownFish, Eel, MantaRay, Salamander)
from attractions import (PettingZoo, Wetlands, SnakePit)

# self.swimming = True - These animals are in the tank
# self.slithering = True - These animals are in the pond
# self.walking = True - These animals are in the petting area
varmint_village = PettingZoo("Varmint Village")
slither_inn = SnakePit("Slither Inn")
blue_cave_cove = Wetlands("Blue Cave Cove")


miss_fuzz = Llama("Miss Fuzz", "domestic llama", "midday", "oats")
alpi = Alpaca("Alpi", "Eastern Alpaca", "morning", "straw")
# print(miss_fuzz)
# miss_fuzz.feed()

mr_worm = KingSnake("Mr. Worm", "common kingsnake", "mice", 5555555)
copper = Copperhead("Copper", "Eastern Copperhead", "eggs", 9999999)
# print(mr_worm)
# mr_worm.feed()

miss_gills = ClownFish("Mrs. Gills", "common clownfish", "kelp")
mr_manta = MantaRay("Mr. Manta", "southern mantaray", "plankton")

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