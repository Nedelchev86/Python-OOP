from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUT_TYPE = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist,
    }

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.success = 0
        self.unsuccess = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if name in [a.name for a in self.astronaut_repository.astronauts]:
            return f"{name} is already added."

        if astronaut_type not in SpaceStation.VALID_ASTRONAUT_TYPE:
            raise Exception("Astronaut type is not valid!")
        astronaut = SpaceStation.VALID_ASTRONAUT_TYPE[astronaut_type](name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if name in [p.name for p in self.planet_repository.planets]:
            return f"{name} is already added."

        item_list = items.split(", ")
        planet = Planet(name)
        planet.items += item_list
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        try:
            astronaut = [a for a in self.astronaut_repository.astronauts if a.name == name][0]
        except IndexError:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        if planet_name not in [p.name for p in self.planet_repository.planets]:
            raise Exception("Invalid planet name!")
        planet = [p for p in self.planet_repository.planets if p.name == planet_name][0]

        try:
            top_5 = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30][0]
        except IndexError:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts = [a for a in sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)]

        top_5_astronauts = [a for a in astronauts if a.oxygen > 30][:5]

        for a in top_5_astronauts:
            while planet.items and a.oxygen > 0:
                collect = planet.items.pop()
                a.backpack.append(collect)
                a.breathe()

        if not planet.items:
            self.success += 1
            return f"Planet: {planet_name} was explored. {len([a for a in top_5_astronauts if a.backpack])} astronauts participated in collecting items."
        else:
            self.unsuccess += 1
            return "Mission is not completed."

    def report(self):

        result = [f"{self.success} successful missions!"]
        result.append(f"{self.unsuccess} missions were not completed!")
        result.append("Astronauts' info:")
        for a in self.astronaut_repository.astronauts:
            result.append(f"Name: {a.name}")
            result.append(f"Oxygen: {a.oxygen}")
            if a.backpack:
                backpack = f"{', '.join(a.backpack)}"
            else:
                backpack = "none"
            result.append(f"Backpack items: {backpack}")

        return "\n".join(result)
