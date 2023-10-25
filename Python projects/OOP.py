class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return (f"Name {self.name} House {self.house}")

    @property
    def house(self):
        return self._house
    @house.setter
    def house(self, house):
        if house not in ["Kala", "Sali", "Nika"]:
            raise ValueError("Not Right!")
        self._house = house
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)



def main():
    argument = Student.get()
    print(argument)

if __name__ == "__main__":
    main()