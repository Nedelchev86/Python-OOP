from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def food_can_eat(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def food_can_eat(self):
        return [Vegetable, Meat, Fruit, Seed]

    @property
    def gained_weight(self):
        return 0.35

