from project.cat import Cat


class Kitten(Cat):
    gender = "Female"

    def __init__(self, name, age,):
        super().__init__(name, age, self.gender)

    @staticmethod
    def make_sound():
        return "Meow"
