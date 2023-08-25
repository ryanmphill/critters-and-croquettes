# import the python datetime module to help us create a timestamp
from datetime import date
from walking import (Llama, Goat, Echidna, Donkey, Alpaca)
from slithering import (Anaconda, Copperhead, CornSnake, KingSnake, RatSnake)
from swimming import (AngelFish, ClownFish, Eel, MantaRay, Salamander)

# self.swimming = True - These animals are in the tank
# self.slithering = True - These animals are in the pond
# self.walking = True - These animals are in the petting area


miss_fuzz = Llama("Miss Fuzz", "domestic llama", "midday", "oats")
print(miss_fuzz)
miss_fuzz.feed()

mr_worm = KingSnake("Mr. Worm", "common kingsnake", "mice")
print(mr_worm)
mr_worm.feed()