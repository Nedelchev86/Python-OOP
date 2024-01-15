from project.cat import Cat


class Kitten(Cat):
    gender = "Famale"

    def __init__(self, name, age):
        super().__init__(name, age, self.gender)
        self.gender = "Female"

    def make_sound(self):
        return "Meow"
