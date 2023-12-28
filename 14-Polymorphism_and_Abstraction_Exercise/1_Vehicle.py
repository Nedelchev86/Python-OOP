from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass
    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        air_condition = 0.9
        consummation = (self.fuel_consumption + air_condition) * distance
        if consummation <= self.fuel_quantity:
            self.fuel_quantity -= consummation

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        air_condition = 1.6
        consummation = (self.fuel_consumption + air_condition) * distance
        if consummation <= self.fuel_quantity:
            self.fuel_quantity -= consummation

    def refuel(self, fuel):
        self.fuel_quantity += (0.95 * fuel)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)