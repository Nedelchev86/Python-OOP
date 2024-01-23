from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."
        self.users.append(User(first_name,  last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"


    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ["PassengerCar", "CargoVan"]:
            return f"Vehicle type {vehicle_type} is inaccessible."
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."
        if vehicle_type == "PassengerCar":
            self.vehicles.append(PassengerCar(brand, model, license_plate_number))
        else:
            self.vehicles.append(CargoVan(brand, model, license_plate_number))

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."


    def allow_route(self,start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True
                continue
        self.routes.append(Route(start_point, end_point, length, len(self.routes)+1))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."


    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        route = [r for r in self.routes if r.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()
        return f"{vehicle.brand} {vehicle.model} License plate: {license_plate_number} Battery: {vehicle.battery_level}% Status: {'Damaged' if vehicle.is_damaged else 'OK'}"

    def repair_vehicles(self, count: int):
        number = 0
        damaged = [d for d in self.vehicles if d.is_damaged]
        sorted_damaged = sorted(damaged, key=lambda x: (x.brand, x.model))
        for v in sorted_damaged:
            if number == count:
                break
            v.is_damaged = False
            v.recharge()
            number += 1
        return f"{number} vehicles were successfully repaired!"


    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: -x.rating)
        result = ["*** E-Drive-Rent ***"]
        [result.append(str(x)) for x in sorted_users]
        return "\n".join(result)


