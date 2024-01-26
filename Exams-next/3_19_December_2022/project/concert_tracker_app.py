from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")
        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")
        musician = self.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")
        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")
        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = [m for m in self.musicians if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a musician!")
        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = [m for m in band.members if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]

        try:
            singer = [s for s in band.members if s.__class__.__name__ == "Singer"][0]
        except IndexError:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        try:
            guitarist = [g for g in band.members if g.__class__.__name__ == "Guitarist"][0]
        except IndexError:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        try:
            drummer = [d for d in band.members if d.__class__.__name__ == "Drummer"][0]
        except IndexError:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        concert = [c for c in self.concerts if c.place == concert_place][0]
        if concert.genre == "Rock":
            if "play the drums with drumsticks" not in drummer.skills or "sing high pitch notes" not in singer.skills or "play rock" not in guitarist.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")

        if concert.genre == "Metal":
            if "play the drums with drumsticks" not in drummer.skills or "sing low pitch notes" not in singer.skills or "play metal" not in guitarist.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")

        if concert.genre == "Jazz":
            if "play the drums with drum brushes" not in drummer.skills or "sing high pitch notes" not in singer.skills or "sing low pitch notes" not in singer.skills or "play jazz" not in guitarist.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")
        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band.name} gained {profit:.2F}$ from the {concert.genre} concert in {concert.place}."
