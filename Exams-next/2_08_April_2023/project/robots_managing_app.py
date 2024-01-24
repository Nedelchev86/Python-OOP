from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type == "MainService":
            self.services.append(MainService(name))
            return f"{service_type} is successfully added."
        elif service_type == "SecondaryService":
            self.services.append(SecondaryService(name))
            return f"{service_type} is successfully added."
        raise Exception("Invalid service type!")

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type == "MaleRobot":
            self.robots.append(MaleRobot(name, kind, price))
            return f"{robot_type} is successfully added."
        elif robot_type == "FemaleRobot":
            self.robots.append(FemaleRobot(name, kind, price))
            return f"{robot_type} is successfully added."
        raise Exception("Invalid robot type!")

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]

        if robot.POSSIBLE_SERVICE != service.__class__.__name__:
            return "Unsuitable service."
        if len(service.robots) >= service.capacity:
            return "Not enough capacity for this robot!"
        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        try:
            robot = [r for r in service.robots if r.name == robot_name][0]
        except IndexError:
            raise Exception("No such robot in this service!")
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."


    def feed_all_robots_from_service(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        [r.eating() for r in service.robots]
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        total = sum(r.price for r in service.robots)
        return f"The value of service {service_name} is {total:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())
        return "\n".join(result)