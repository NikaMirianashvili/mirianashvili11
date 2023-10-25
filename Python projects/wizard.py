class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name!")
        self.name = name

    def __str__(self):
        return f"Hello my name is {self.name}"

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    def get_name(self):
        return self.house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def get_subject(self):
        return self.subject

student = Student("Harry", "Location 1")
professor = Professor("Sali", "Mexaniki")
print(student.get_name())
print(professor.get_subject())