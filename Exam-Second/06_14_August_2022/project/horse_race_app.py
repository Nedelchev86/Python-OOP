from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred,
    }

    RACES_ADDED = []

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type in HorseRaceApp.VALID_HORSES:
            self.horses.append(HorseRaceApp.VALID_HORSES[horse_type](horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in HorseRaceApp.RACES_ADDED:
            raise Exception(f"Race {race_type} has been already created!")
        HorseRaceApp.RACES_ADDED.append(race_type)
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = [j for j in self.jockeys if j.name == jockey_name][0]
        except IndexError:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = [h for h in self.horses if h.__class__.__name__ == horse_type and not h.is_taken][-1]
        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey.name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        if race_type not in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = [j for j in self.jockeys if j.name == jockey_name][0]
        except IndexError:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        h_race = [race for race in self.horse_races if race.race_type == race_type][0]
        if jockey in h_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        h_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        try:
            race = [r for r in self.horse_races if r.race_type == race_type][0]
        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        high_speed = 0
        fastest = ""
        for jockeys in  race.jockeys:
            if jockeys.horse.speed > high_speed:
                high_speed = jockeys.horse.speed
                fastest = jockeys
        return f"The winner of the {race_type} race, with a speed of {high_speed}km/h is {fastest.name}! Winner's horse: {fastest.horse.name}."


    