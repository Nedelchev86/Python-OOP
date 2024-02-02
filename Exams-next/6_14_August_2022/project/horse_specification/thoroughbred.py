from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    MAXIMUM_SPEED = 140

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        try:
            self.speed += 3
        except ValueError:
            self.speed = self.MAXIMUM_SPEED
