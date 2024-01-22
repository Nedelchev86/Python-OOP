from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type == "Appaloosa":
            self.horses.append(Appaloosa(horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."
        elif horse_type == "Thoroughbred":
            self.horses.append(Thoroughbred(horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for jokey in self.jockeys:
            if jokey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")
        jokey = Jockey(jockey_name, age)
        self.jockeys.append(jokey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for races in self.horse_races:
            if races.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = None
        for j in self.jockeys:
            if j.name == jockey_name:
                jockey = j
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = None
        for h in self.horses:
            if h.__class__.__name__ == horse_type:
                if not h.is_taken:
                    horse = h

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = None
        jokey = None
        for races in self.horse_races:
            if races.race_type == race_type:
                race = races
        if not race:
            raise Exception("Race {race_type} could not be found!")
        for jokeys in self.jockeys:
            if jokeys.name == jockey_name:
                jokey = jokeys
        if not jokey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not jokey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        for j in self.jockeys:
            if jokey in j.jockeys:
                raise Exception("Jockey {jockey_name} has been already added to the {race_type} race.")
        self.horse_races.append(HorseRace(jokey))
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        pass