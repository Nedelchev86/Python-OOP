from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):

    max_mileage = 450.00

    def __init__(self, brand, model, license_plate_number):
        super().__init__(brand, model, license_plate_number, PassengerCar.max_mileage)

    def drive(self, mileage: float):
        result = round((mileage / PassengerCar.max_mileage) * 100)
        self.battery_level -= result

