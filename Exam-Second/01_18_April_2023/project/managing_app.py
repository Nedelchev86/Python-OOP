from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_CAR_TYPES = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan,
    }

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if driving_license_number in [u.driving_license_number for u in self.users if u.driving_license_number == driving_license_number]:
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ManagingApp.VALID_CAR_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if license_plate_number in [v.license_plate_number for v in self.vehicles if v.license_plate_number == license_plate_number]:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(ManagingApp.VALID_CAR_TYPES[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

        route_id = len(self.routes) + 1
        route = Route(start_point, end_point, length, route_id)

        self.routes.append(route)

        for r in self.routes:
            if r.start_point == route.start_point and r.end_point == route.end_point and r.length > route.length:
                r.is_locked = True
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
        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged = [v for v in self.vehicles if v.is_damaged]
        repaired = 0
        for vehicle in sorted(damaged, key=lambda x: (x.brand, x.model)):
            if count == repaired:
                break
            vehicle.recharge()
            vehicle.change_status()
            repaired += 1
        return f"{repaired} vehicles were successfully repaired!"

    def users_report(self):
        users_by_rating = list(sorted(self.users, key=lambda x: -x.rating))
        result = ["*** E-Drive-Rent ***"]
        [result.append(str(u)) for u in users_by_rating]
        return "\n".join(result)

