from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    max_mileage = 180.00

    def __init__(self, brand, model, license_plate_number):
        super().__init__(brand, model, license_plate_number, CargoVan.max_mileage)

    def drive(self, mileage: float):
        result = round((mileage / CargoVan.max_mileage) * 100 + 5)
        self.battery_level -= result

