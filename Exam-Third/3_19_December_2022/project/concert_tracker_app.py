from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer,
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN:
            raise ValueError("Invalid musician type!")
        if name in [m.name for m in  self.musicians]:
            raise Exception(f"{name} is already a musician!")
        self.musicians.append(self.VALID_MUSICIAN[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in [b.name for b in  self.bands]:
            raise Exception(f"{name} band is already created!")
        self.bands.append(Band(name))
        return f"{name} was created."
    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if place in [c.place for c in self.concerts]:
            concert = [c for c in self.concerts if c.place == place][0]
            raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")
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
        concert = [c for c in self.concerts if c.place == concert_place][0]
        band = [b for b in self.bands if b.name == band_name][0]

        all_type = [m.__class__.__name__ for m in self.musicians]
        if "Guitarist" not in all_type or "Drummer" not in all_type or "Singer" not in all_type:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        drummer = [d for d in self.musicians if d.__class__.__name__ == "Drummer"][0]
        guitarist = [d for d in self.musicians if d.__class__.__name__ == "Guitarist"][0]
        singer = [d for d in self.musicians if d.__class__.__name__ == "Singer"][0]

        if concert.genre == "Rock":
            if "play the drums with drumsticks" not in drummer.skills or "sing high pitch notes" not in singer.skills or "play rock" not in guitarist.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")
        elif concert.genre == "Metal":
            if "play the drums with drumsticks" not in drummer.skills or "sing low pitch notes" not in singer.skills or "play metal" not in guitarist.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")
        elif concert.genre == "Jazz":
            if "play the drums with drum brushes" not in drummer.skills or "sing high pitch notes" not in singer.skills or "sing low pitch notes" not in singer.skills or "play jazz" not in guitarist.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")

        return f"{band.name} gained {(concert.audience * concert.ticket_price) - concert.expenses:.2F}$ from the {concert.genre} concert in {concert.place}."