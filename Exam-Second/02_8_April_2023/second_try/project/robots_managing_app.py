from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService,
    }

    VALID_ROBOTS = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot,
    }

    def __init__(self) -> None:
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in RobotsManagingApp.VALID_SERVICES:
            raise Exception("Invalid service type!")

        self.services.append(RobotsManagingApp.VALID_SERVICES[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in RobotsManagingApp.VALID_ROBOTS:
            raise Exception("Invalid robot type!")
        self.robots.append(RobotsManagingApp.VALID_ROBOTS[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if robot_name == r.name][0]
        service = [s for s in self.services if service_name == s.name][0]

        if robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "MainService":
            return "Unsuitable service."

        if robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "SecondaryService":
            return "Unsuitable service."

        if service.capacity == len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."


    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [s for s in self.services if service_name == s.name][0]

        try:
            robot = [r for r in service.robots if r.name == robot_name][0]
        except IndexError:
            raise Exception("No such robot in this service!")

        self.robots.append(robot)
        service.robots.remove(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = [s for s in self.services if service_name == s.name][0]
        count = 0

        for r in service.robots:
            r.eating()
            count += 1
        return f"Robots fed: {count}."


    def service_price(self, service_name: str):
        service = [s for s in self.services if service_name == s.name][0]
        price = 0
        for r in service.robots:
            price += r.price
        return f"The value of service {service_name} is {price:.2F}."

    def __str__(self):
        result = []
        for s in self.services:
            result.append(s.details())

        return "\n".join(result)