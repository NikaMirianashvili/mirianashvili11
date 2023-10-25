import random

class Hat:
    houses = ["Location 1", "Location 2", "Location 3", "Location 4"]

    @classmethod
    def sort(cls,name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Sali")

