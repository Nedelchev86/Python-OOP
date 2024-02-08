from project.car.car import Car


class SportsCar(Car):
    min_speed_limit = 400
    max_speed_limit = 600

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value < SportsCar.min_speed_limit or value > SportsCar.max_speed_limit:
            raise ValueError(f"Invalid speed limit! Must be between {SportsCar.min_speed_limit} and {SportsCar.max_speed_limit}!")
        self.__speed_limit = value

