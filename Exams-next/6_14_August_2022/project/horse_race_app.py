from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPE = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}
    CREATED_RACE = []

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.VALID_HORSE_TYPE:
            return

        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        self.horses.append(self.VALID_HORSE_TYPE[horse_type](horse_name, horse_speed))
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in self.CREATED_RACE:
            raise Exception(f"Race {race_type} has been already created!")
        self.CREATED_RACE.append(race_type)
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = [j for j in self.jockeys if j.name == jockey_name][0]
        except IndexError:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = [h for h in reversed(self.horses) if h.__class__.__name__ == horse_type and not h.is_taken][0]
        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            horse_race = [r for r in self.horse_races if r.race_type == race_type][0]
        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")
        try:
            jockey = [j for j in self.jockeys if j.name == jockey_name][0]
        except IndexError:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        if race_type not in self.CREATED_RACE:
            raise Exception(f"Race {race_type} could not be found!")
        race = [r for r in self.horse_races if r.race_type == race_type][0]
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        # max_speed_horse = 0
        # best_jockey = None
        #
        # for jockey in race.jockeys:
        #     if jockey.horse.speed > max_speed_horse:
        #         best_jockey = jockey
        #         max_speed_horse = jockey.horse.speed

        best_jockey = sorted(race.jockeys, key=lambda jockey: -jockey.horse.speed)[0]

        return f"The winner of the {race_type} race, with a speed of {best_jockey.horse.speed}km/h is {best_jockey.name}! Winner's horse: {best_jockey.horse.name}."

