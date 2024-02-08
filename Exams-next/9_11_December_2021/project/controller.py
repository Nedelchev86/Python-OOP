from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    CAR_TYPE = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __find_race(self, race_name):
        try:
            race = [r for r in self.races if r.name == race_name][0]
        except IndexError:
            raise Exception(f"Race {race_name} could not be found!")
        return race

    def __find_driver(self, driver_name):
        try:
            driver = [d for d in self.drivers if d.name == driver_name][0]
        except IndexError:
            raise Exception(f"Driver {driver_name} could not be found!")
        return driver

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in self.CAR_TYPE:
            for car in self.cars:
                if car.model == model:
                    raise Exception(f"Car {model} is already created!")
            self.cars.append(self.CAR_TYPE[car_type](model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver(driver_name)

        try:
            car = [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken][-1]
        except IndexError:
            raise Exception(f"Car {car_type} could not be found!")
        if driver.car:
            old_car_model = driver.car.model
            driver.car.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_car_model} to {driver.car.model}."
        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race(race_name)
        driver = self.__find_driver(driver_name)

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race(race_name)

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        count = 0
        fastest = list(sorted(race.drivers, key=lambda x: -x.car.speed_limit))
        result = []

        for d in fastest:
            count += 1
            d.number_of_wins += 1
            result.append(f"Driver {d.name} wins the {race_name} race with a speed of {d.car.speed_limit}.")
            if count == 3:
                break
        return "\n".join(result)