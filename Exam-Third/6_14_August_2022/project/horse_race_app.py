from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred,
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type not in self.VALID_HORSES:
            return
        self.horses.append(self.VALID_HORSES[horse_type](horse_name, horse_speed))
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")
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
            return f"Jockey {jockey.name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."


    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            race = [r for r in self.horse_races if r.race_type == race_type][0]
        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = [j for j in self.jockeys if j.name == jockey_name][0]
        except IndexError:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        for r in self.horse_races:
            if jockey in r.jockeys:
                return f"Jockey {jockey_name} has been already added to the {r.race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        try:
            race = [r for r in self.horse_races if r.race_type == race_type][0]
        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race.race_type} needs at least two participants!")

        fastest_horse = 0
        fastest_jockey = ""

        for j in race.jockeys:
            if j.horse.speed > fastest_horse:
                fastest_horse = j.horse.speed
                fastest_jockey = j

        return f"The winner of the {race_type} race, with a speed of {fastest_horse}km/h is {fastest_jockey.name}! Winner's horse: {fastest_jockey.horse.name}."
